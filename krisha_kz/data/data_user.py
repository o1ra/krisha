from krisha_kz.users.user import User

user_rent = User(
    buy_or_rent='Арендовать',
    categories_for_rent='квартиру',
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

user_buy = User(
    buy_or_rent='Купить',
    categories_for_rent='квартиру',
    city='Алматы',
    area='Ауэзовский р-н',
    number_of_rooms='1 - комн.',
    prise_min="100000",
    prise_max="500000",
    checkbox_photo=True,
    checkbox_new_buildings=True,
    checkbox_agents=True,
    checkbox_owner=True
)
