import os
from typing import Literal
import pydantic
from krisha_kz.utils import path


BrowserType = Literal['chrome', 'firefox']
EnvContext = Literal['local', 'test', 'stage']


class Config(pydantic.BaseSettings):
    # --- User Aurh ---
    data: str = os.getenv("data", "user_rent")

    # --- Browser ---
    base_url: str = 'https://krisha.kz'
    hold_driver_at_exit: bool = False
    remote_driver_url: str = os.getenv("REMOTE_DRIVER_URL")
    driver_name: BrowserType = os.getenv("driver_name", 'chrome')
    version: str = os.getenv("version", '100.0')
    headless: bool = os.getenv("headless", 'False')
    timeout: float = float(os.getenv("timeout", '15.0'))
    window_width: int = int(os.getenv("window_width", '1024'))
    window_height: int = int(os.getenv("window_height", '768'))

    # --- Context ---
    context: EnvContext = 'local'


context = Config().context
config = Config(_env_file=path.to_resource(f'.env.{context}'))


