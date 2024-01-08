import allure
from allure_commons.types import Severity
from selene import browser, by, be
from krisha_kz.data import data_user
from krisha_kz.model.main_page import SearchPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Поиск")
@allure.story("Выполнение поиска без авторизации по умолчанию")
@allure.link("https://krisha.kz", name="Testing")
def test_default_search():
    search_page = SearchPage()

    with allure.step("Открываем главную страницу"):
        search_page.open()

    with allure.step("Выполняем поиск по умолчанию по карте"):
        search_page.map_search()

    with allure.step("Закрываем модальное окно"):
        search_page.close_modal()

    with allure.step("Проверяем наличие текста 'Показать результаты' на кнопке"):
        search_page.check_search_btn_text()

    with allure.step("Проверяем наличие карты"):
        search_page.check_map()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Поиск")
@allure.story("Выполнение поиска покупки квартиры ")
@allure.link("https://krisha.kz", name="Testing")
def test_search():
    search_page = SearchPage()

    with allure.step("Открываем главную страницу"):
        search_page.open()

    with allure.step("Выбираем пункт аренда"):
        search_page.select_category_type(data_user.buy_or_rent)

    with allure.step("Выбираем категорию"):
        search_page.select_categories_for_rent(data_user.categories_for_rent)

    with allure.step("Выбираем город и район"):
        search_page.select_city(data_user.city)
        search_page.select_region(data_user.area)

    with allure.step("Выбираем количество комнат"):
        search_page.select_the_number_of_rooms(data_user.number_of_rooms)

    with allure.step("Выбираем диапазон цен"):
        search_page.prise_min(data_user.prise_min)
        search_page.prise_max(data_user.prise_max)

    with (allure.step("Выбираем чекбоксы")):
        if data_user.checkbox_photo:
            search_page.checkbox_photo()

        if data_user.checkbox_new_buildings:
            search_page.checkbox_new_buildings()

        if data_user.checkbox_agents:
            search_page.checkbox_agents()

        if data_user.checkbox_owner:
            search_page.checkbox_owner()

        with allure.step("Выполняем поиск"):
            search_page.search_btn_blue()

        with allure.step("Закрываем модальное окно"):
            search_page.close_modal()

        with allure.step("Проверяем наличие текста 'Показать результаты' на кнопке"):
            search_page.check_search_btn_text()

        with allure.step("Проверяем наличие элементов в выдаче"):
            assert len(browser.all('.a-search-list [data-id]')) > 0
