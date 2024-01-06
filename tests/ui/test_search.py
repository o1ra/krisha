import allure
from allure_commons.types import Severity
from selene import browser, have, by, be
from krisha_kz.data import data_user
from krisha_kz.model.main_page import SearchPage


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Поиск")
@allure.story("Выполнение поиска без авторизации по умолчанию")
@allure.link("https://krisha.kz", name="Testing")
def test_default_search():
    with allure.step("Открываем главную страницу"):
        browser.open('/')

    with allure.step("Выполняем поиск по умолчанию по карте"):
        browser.element('.map-search').click()

    with allure.step("Закрываем модальное окно"):
        browser.element('.fi-close-big').double_click()

    with allure.step("Проверяем наличие текста 'Показать результаты' на кнопке"):
        browser.element('.kr-btn--blue').element(by.text("Показать результаты"))

    with allure.step("Проверяем наличие карты"):
        browser.element('.map-canvas').should(be.visible)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
@allure.link("https://krisha.kz", name="Testing")
def test_link_selling():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Продажа")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/prodazha/'))

    with allure.step("Цены на недвижимость в Казахстане: горячие предложения'"):
        browser.element(".hot-header").should(
            have.text("Цены на недвижимость в Казахстане: горячие предложения"))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
def test_link_rent():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Аренда")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/arenda/'))

    with allure.step("Цены на аренду недвижимости в Казахстане: горячие предложения"):
        browser.element(".hot-header").should(
            have.text("Цены на аренду недвижимости в Казахстане: горячие предложения"))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
def test_link_valuation():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Оценка")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/valuation/'))

    with allure.step("Узнайте за какую цену продать, сдать или купить квартиру"):
        browser.element(".valuation-h1").should(
            have.text("Узнайте за какую цену продать, сдать или купить квартиру"))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
def test_link_seach():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Новостройки")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/complex/search/'))

    with allure.step("Новостройки в Казахстане"):
        browser.element(".heading").should(
            have.text("Новостройки в Казахстане"))

        browser.element('.complex-fast-filter__item--selected').element(by.text('ЖК в продаже'))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
def test_link_news():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Новости")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/content/'))

    # with allure.step(""):
    #     browser.element(".").should(
    #         have.text(""))


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Irina_Kirillova")
@allure.feature("Ссылки")
@allure.story("Переход по ссылкам меню")
def test_link_guide():
    browser.open('/')

    browser.element('.main-menu').element(by.text("Крыша Гид")).click()

    with allure.step("Проверяем URL'"):
        browser.should(
            have.url('https://krisha.kz/guide/'))

    with allure.step(""):
        browser.element(".guide-promo__title").should(
            have.text("Крыша Гид"))


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
            browser.element('.kr-btn--blue').click()

        with allure.step("Закрываем модальное окно"):
            browser.element('.fi-close-big').double_click()

        with allure.step("Проверяем наличие текста 'Показать результаты' на кнопке"):
            browser.element('.kr-btn--blue').element(by.text("Показать результаты"))

        with allure.step("Проверяем наличие элементов в выдаче"):
            assert len(browser.all('.a-search-list [data-id]')) > 0
