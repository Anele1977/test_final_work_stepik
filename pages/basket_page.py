from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_about_product_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_PRODUCT_IN_BASKET_ON_MAIN_PAGE), "Not find message 'in basket not product' "

    def should_be_not_product_in_basket(self):
        assert self.element_is_not_present(*BasketPageLocators.PRODUCT_NAME_IN_BASKET), "Product in basket"
