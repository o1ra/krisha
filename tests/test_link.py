import allure
from allure_commons.types import Severity
from krisha_kz.model.main_menu import MainMenu


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Продажа")
@allure.link("https://krisha.kz", name="Testing")
def test_link_selling():
    main_menu = MainMenu()
    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Продажа'"):
        main_menu.item_menu("Продажа")

    with allure.step("Проверяем URL'"):
        main_menu.check_url("https://krisha.kz/prodazha/")

    with allure.step("Цены на недвижимость в Казахстане: горячие предложения"):
        main_menu.check_text("Цены на недвижимость в Казахстане: горячие предложения")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Аренда")
def test_link_rent():
    main_menu = MainMenu()

    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Аренда'"):
        main_menu.item_menu("Аренда")

    with allure.step("Проверяем URL'"):
        main_menu.check_url('https://krisha.kz/arenda/')

    with allure.step("Цены на аренду недвижимости в Казахстане: горячие предложения"):
        main_menu.check_text("Цены на аренду недвижимости в Казахстане: горячие предложения")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Оценка")
def test_link_valuation():
    main_menu = MainMenu()

    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Оценка'"):
        main_menu.item_menu("Оценка")

    with allure.step("Проверяем URL'"):
        main_menu.check_url('https://krisha.kz/valuation/')

    with allure.step("Узнайте за какую цену продать, сдать или купить квартиру"):
        main_menu.title_grade()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Новостройки")
def test_link_seach():
    main_menu = MainMenu()

    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Новостройки'"):
        main_menu.item_menu("Новостройки")

    with allure.step("Проверяем URL'"):
        main_menu.check_url('https://krisha.kz/complex/search/')

    with allure.step('Заголовок: "Новостройки в Казахстане"'):
        main_menu.title_new_bildings()

    with allure.step("Выбран пункт 'ЖК в продаже'"):
        main_menu.item_new_bildings()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Новости")
def test_link_news():
    main_menu = MainMenu()

    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Новости'"):
        main_menu.item_menu("Новости")

    with allure.step("Проверяем URL'"):
        main_menu.check_url('https://krisha.kz/content/')

    with allure.step("Заголовок: 'Новости'"):
        main_menu.title_news()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
@allure.feature("Главное меню")
@allure.story("Крыша Гид")
def test_link_guide():
    main_menu = MainMenu()

    with allure.step("Открываем главную страницу"):
        main_menu.open()

    with allure.step("Выбираем пункт меню 'Крыша Гид'"):
        main_menu.item_menu("Крыша Гид")

    with allure.step("Проверяем URL'"):
        main_menu.check_url('https://krisha.kz/guide/')

    with allure.step("Заголовок: 'Крыша Гид'"):
        main_menu.item_new_bildings()
