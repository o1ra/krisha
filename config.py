from typing import Literal
import pydantic
from krisha_kz.utils import path


BrowserType = Literal['chrome', 'firefox']
EnvContext = Literal['local', 'test', 'stage']
User = Literal['user_buy', 'user_rent']


class Config(pydantic.BaseSettings):
    # --- User Aurh ---
    data: User = None

    # --- Browser ---
    base_url: str = 'https://krisha.kz'
    driver_name: BrowserType = 'chrome'
    version = '100.0'
    hold_driver_at_exit: bool = False
    window_width: int = 1024
    window_height: int = 768
    timeout: float = 15.0
    headless: bool = False

    # --- Context ---
    context: EnvContext = 'local'


context = Config().context
config = Config(_env_file=path.to_resource(f'.env.{context}'))


