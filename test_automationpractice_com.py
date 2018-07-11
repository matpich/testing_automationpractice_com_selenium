from selenium import webdriver
from pages import page
import pytest
import time

@pytest.fixture(scope='class')
def home_page():
    '''Set driver and HomePage object.'''
    driver = webdriver.Chrome()
    driver.get('http://automationpractice.com/index.php')
    return page.HomePage(driver)

class TestHomePage():
    '''Tests home page elements.'''

    def test_cart(self,home_page):
        '''Checks if shopping cart is opened correctly.'''
        home_page.click_cart()
        #Checks if title is correct
        assert home_page.cart_title_match()

    @pytest.mark.parametrize('search_val', [('dress'),('shirt'),('blouse'),])
    def test_search_box(self, home_page, search_val):
        '''Shoots search box with some values.'''
        home_page.search_value = search_val
        home_page.input_into_search_box()
        home_page.click_search_button()
        assert home_page.search_any_results()

