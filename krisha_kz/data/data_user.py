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


user_buy = User(
    buy_or_rent='Купить',
    categories_for_sell='квартиру',
    categories_for_rent='',
    city='Алматы',
    area='Ауэзовский р-н',
    number_of_rooms='1 - комн.',
    prise_min="10000000",
    prise_max="50000000",
    checkbox_photo=True,
    checkbox_new_buildings=True,
    checkbox_agents=True,
    checkbox_owner=True
)


user_rent = User(
    buy_or_rent='Арендовать',
    categories_for_rent='квартиру',
    categories_for_sell='',
    city='Алматы',
    area='Ауэзовский р-н',
    number_of_rooms='1 - комн.',
    prise_min="100000",
    prise_max="500000",
    checkbox_photo=True,
    checkbox_new_buildings=False,
    checkbox_agents=False,
    checkbox_owner=True
)

