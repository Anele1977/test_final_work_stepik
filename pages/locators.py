from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_ON_SEE_PAGE = (By.CSS_SELECTOR, "span > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    EMAIL_FILD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FILD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FILD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[value='Register']")

class LoginPageLocators:
    URL_FORM = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')

    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')

class BasketPageLocators:
    MESSAGE_ABOUT_PRODUCT_IN_BASKET_ON_MAIN_PAGE = (By.CSS_SELECTOR, "div#content_inner")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div .col-sm-4 > a")

