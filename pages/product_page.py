from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_basket_find = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button_basket_find.click()

    # метод проверки сообщения с названием ном-ры
    def should_be_message_book(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text == \
                self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text, "В корзину добавилась не та ном-ра"

    # метод проверки прайса корзины с ценой товара
    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text == \
                self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Цена добавленного в корзину товара не совпадает"

    # проверяет, что элемент не появляется на странице в течение заданного времени:
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # проверить, что какой-то элемент исчезает
    def should_see_as_disappearing(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but it must disappear"













