from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BASKET_BUTTON)
        add_to_basket_btn.click()

    def should_be_add_to_basket_message(self):
        name_product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BASKET_SUCCESS_MESS).text
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_product == name_product_in_message, f'Expect {name_product} in success message, got {name_product_in_message}'

    def should_not_be_add_to_basket_message(self):
        check_success_message = self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET_SUCCESS_MESS)
        assert check_success_message, f'Not expect a success message add basket, got a success message'

    def should_not_be_add_to_basket_message_at_product_page(self):
        check_success_message = self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_BASKET_SUCCESS_MESS)
        assert check_success_message, f'Not expect a success message add basket, got a success message'

    def should_disappear_add_to_basket_message(self):
        disappear_success_message = self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_BASKET_SUCCESS_MESS)
        assert disappear_success_message, f'Expect disappear message add basket, got not disappear message'

    def should_be_product_cost_equal_basket_cost(self):
        basket_cost_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_BASKET_COST_MESS).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        assert product_cost == basket_cost_in_message, f'Expect {product_cost} in success message, got {basket_cost_in_message}'