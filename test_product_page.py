from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


link_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
link_user_product_page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_message()
    page.should_be_product_cost_equal_basket_cost()

@pytest.mark.xfail(reason="known message issue")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_add_to_basket_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.should_not_be_add_to_basket_message_at_product_page()

@pytest.mark.xfail(reason="known message disappear issue")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_product_page)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_add_to_basket_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_empty()

@pytest.mark.user_work_with_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        #prepare test data
        email_test_data, password_test_data = page.prepare_register_test_data()
        #setup step
        page.open()
        page.register_new_user(email_test_data, password_test_data)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link_user_product_page)
        page.open()
        page.add_product_to_basket()
        page.should_be_add_to_basket_message()
        page.should_be_product_cost_equal_basket_cost()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_user_product_page)
        page.open()
        page.should_not_be_add_to_basket_message_at_product_page()
