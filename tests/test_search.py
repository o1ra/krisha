import os
import allure
from allure_commons.types import Severity
from selene import browser
from krisha_kz.model.main_page import SearchPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.label('layer', 'UI')
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
@allure.label('layer', 'UI')
@allure.feature("Поиск")
@allure.story("Выполнение поиска покупки квартиры ")
@allure.link("https://krisha.kz", name="Testing")
def test_search(data):

    search_page = SearchPage()

    with allure.step("Открываем главную страницу"):
        search_page.open()

    with allure.step("Выбираем пункт аренда или покупка"):
        search_page.select_category_type(data.buy_or_rent)

    with allure.step("Выбираем категорию жилья"):
        if os.getenv("data") == "user_rent":
            search_page.select_categories_for_rent(data.categories_for_rent)
        else:
            search_page.select_categories_for_sell(data.categories_for_sell)

    with allure.step("Выбираем город и район"):
        search_page.select_city(data.city)
        search_page.select_region(data.area)

    with allure.step("Выбираем количество комнат"):
        search_page.select_the_number_of_rooms(data.number_of_rooms)

    with allure.step("Выбираем диапазон цен"):
        search_page.prise_min(data.prise_min)
        search_page.prise_max(data.prise_max)

    with (allure.step("Выбираем чекбоксы")):
        if data.checkbox_photo:
            search_page.checkbox_photo()

        if data.checkbox_new_buildings:
            search_page.checkbox_new_buildings()

        if data.checkbox_agents:
            search_page.checkbox_agents()

        if data.checkbox_owner:
            search_page.checkbox_owner()

        with allure.step("Выполняем поиск"):
            search_page.search_btn_blue()

        with allure.step("Закрываем модальное окно"):
            search_page.close_modal()

        with allure.step("Проверяем наличие текста 'Показать результаты' на кнопке"):
            search_page.check_search_btn_text()

        with allure.step("Проверяем наличие элементов в выдаче"):
            assert len(browser.all('.a-search-list [data-id]')) > 0
