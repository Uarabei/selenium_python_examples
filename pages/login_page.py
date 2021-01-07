from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, 'Url login page haven`t got word "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login form email input is not visible"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login form password input is not visible"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login form Login button is not visible"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register form email input is not visible"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "Register form password input is not visible"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM), "Register form password confirm input is not visible"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register form Registration button is not visible"