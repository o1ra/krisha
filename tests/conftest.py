import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selene import browser
from krisha_kz_tests.utils import attach, path
from config import config
from krisha_kz_tests.data.data_user import user_rent, user_buy


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        action="store",
        default="local",
        choices=["local", "test", "prod"],
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = path.to_resource(f".env.{context}")

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture(scope="session")
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope="session")
def data():
    data_type = os.getenv("data")
    if data_type == "user_rent":
        return user_rent
    elif data_type == "user_buy":
        return user_buy
    else:
        raise ValueError(f"Unsupported data type: {data_type}")


@pytest.fixture(scope="function", autouse=True)
def browser_management(request, context):
    browser.config.base_url = config.base_url
    browser.config.driver_name = config.driver_name
    browser.config.version = config.version
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    options = Options()

    if config.headless:
        if browser.config.driver_name == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser.config.driver_name == 'firefox':
            options = webdriver.FirefoxOptions()
        else:
            raise ValueError(f"Unsupported browser: {browser.config.driver_name}")

        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        browser.config.driver_options = options

    if context == 'test' or context == 'prod':
        selenoid_capabilities = {
            "browserName": browser.config.driver_name,
            "browserVersion": browser.config.version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options.capabilities.update(selenoid_capabilities)
        remote_driver_url = os.getenv('REMOTE_DRIVER_URL')
        driver = webdriver.Remote(
            command_executor=remote_driver_url,
            options=options
        )
        browser.config.driver = driver
    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    if browser.config.driver_name == "chrome":
        attach.add_logs(browser)
    browser.quit()
