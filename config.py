from typing import Literal
import pydantic
from krisha_kz.utils import path

BrowserType = Literal['chrome', 'firefox', 'edge']
EnvContext = Literal['local', 'test', 'stage']


class Config(pydantic.BaseSettings):

    # --- User Aurh ---
    buy_or_rent: str = None
    categories_for_rent: str = None
    city: str = None
    area: str = None
    number_of_rooms: str = None
    prise_min: int = 1
    prise_max: int = 100000000
    checkbox_photo: bool = 'false'
    checkbox_new_buildings: bool = 'false'
    checkbox_agents: bool = 'False'
    checkbox_owner: bool = 'False'

    # --- Context ---
    context: EnvContext = 'test'

    # --- Browser ---
    base_url: str = 'https://krisha.kz'
    driver_name: BrowserType = 'chrome'
    version = '100.0'
    hold_driver_at_exit: bool = False
    window_width: int = 1024
    window_height: int = 768
    timeout: float = 10.0
    headless: bool = False


context = Config().context
config = Config(_env_file=path.to_resource('.env' if context == 'local' else f'.env.{context}'))
