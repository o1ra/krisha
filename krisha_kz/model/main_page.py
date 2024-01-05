from selene import by
from selene.support.shared import browser


class SearchPage:
    def __int__(self):
        pass

    def open(self):
        browser.open('/')
        return self

    def select_category_type(self, buy_or_rent):
        browser.element('.category-type').click().element(by.text(buy_or_rent)).click()
        return self

    def select_categories_for_rent(self, categories_for_rent):
        browser.element('.categories-for-rent').click().element(by.text(categories_for_rent)).click()
        return self

    def select_city(self, city: str):
        browser.element('.region-dropdown-label').click()
        browser.element('.element-region-dropdown-inner').element(by.text(city)).click()
        return self

    def select_region(self, area: str):
        browser.element('.element-region-dropdown-inner').element(by.text(area)).click()
        browser.element('.element-region-dropdown-inner').element('.btn-primary:not(.is-disabled)').click()
        return self

    def select_the_number_of_rooms(self, number_of_rooms: str):
        browser.element('.specs_kvartiry [name="das[live.rooms]"]').click().element(
            by.text(number_of_rooms)).click()
        return self

    def prise_min(self, prise_min: int):
        browser.element('.search-element-price [placeholder="От"]').type(prise_min)
        return self

    def prise_max(self, prise_max: int):
        browser.element('.search-element-price [placeholder="До"]').type(prise_max)
        return self

    def checkbox_photo(self):
        browser.element(".checkbox-conditions").element(by.text("есть фото")).click()
        return self

    def checkbox_new_buildings(self):
        browser.element(".checkbox-conditions").element(by.text("новостройки")).click()
        return self

    def checkbox_agents(self):
        browser.element(".checkbox-conditions").element(by.text("От Крыша Агентов")).click()
        return self

    def checkbox_owner(self):
        browser.element(".checkbox-conditions").element(by.text("от хозяев")).click()
        return self
