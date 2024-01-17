from selene import browser, by, have


class MainMenu:
    def __int__(self):
        pass

    def open(self):
        browser.open('/')
        return self

    def item_menu(self, item):
        browser.element('.main-menu').element(by.text(item)).click()
        return self

    def check_url(self, url):
        browser.should(have.url(url))
        return self

    def check_text(self, text):
        browser.element(".hot-header").should(have.text(text))
        return self

    def item_new_bildings(self):
        browser.element('.complex-fast-filter__item--selected').element(by.text('ЖК в продаже'))
        return self

    def title_new_bildings(self):
        browser.element(".heading").should(
            have.text("Новостройки в Казахстане"))
        return self

    def title_news(self):
        browser.element(".content-news .title").should(have.text("Новости"))
        return self

    def title_grade(self):
        browser.element(".valuation-h1").should(
            have.text("Узнайте за какую цену продать, сдать или купить квартиру"))
        return self


main_menu = MainMenu()
