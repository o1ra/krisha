import dataclasses


@dataclasses.dataclass
class User:
    buy_or_rent: str
    categories_for_rent: str
    categories_for_sell: str
    city: str
    area: str
    number_of_rooms: str
    prise_min: str
    prise_max: str
    checkbox_photo: bool
    checkbox_new_buildings: bool
    checkbox_agents: bool
    checkbox_owner: bool



