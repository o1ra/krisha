import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
import config
from krisha_kz.utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_management():
    browser.config.base_url = config.config.base_url
    browser.config.driver_name = config.config.driver_name
    browser.config.version = config.config.version
    browser.config.hold_driver_at_exit = config.config.hold_driver_at_exit
    browser.config.window_width = config.config.window_width
    browser.config.window_height = config.config.window_height
    browser.config.timeout = config.config.timeout

    if config.context == 'test' or 'prod':
        options = Options()

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

        browser.config.driver = webdriver.Remote(
            command_executor=f"{remote_driver_url}",
            options=options,
        )

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
