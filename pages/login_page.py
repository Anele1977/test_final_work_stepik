import time

from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "not found this phrases in url"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        email_fild = self.browser.find_element(*BasePageLocators.EMAIL_FILD)
        email_fild.send_keys(email)
        password_fild_1 = self.browser.find_element(*BasePageLocators.PASSWORD_FILD_1)
        password_fild_1.send_keys(password)
        password_fild_2 = self.browser.find_element(*BasePageLocators.PASSWORD_FILD_2)
        password_fild_2.send_keys(password)
        button_register = self.browser.find_element(*BasePageLocators.BUTTON_REGISTER)
        button_register.click()




