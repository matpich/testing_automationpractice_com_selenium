from selenium import webdriver
from pages import page
import pytest
import time

@pytest.fixture(scope="session")
def set_driver():
    web_driver =  webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    web_driver.close()

@pytest.fixture(scope='class')
def home_page(set_driver):
    '''Return HomePage object.'''
    set_driver.get('http://automationpractice.com/index.php')
    return page.HomePage(set_driver)

@pytest.fixture(scope='class')
def authentication_page(set_driver):
    '''Return AuthenticationPage object.'''
    set_driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
    return page.AuthenticationPage(set_driver)

@pytest.fixture(scope='class')
def registration_page(set_driver):
    '''Return RegistrationPage object.'''
    set_driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
    return page.RegistrationPage(set_driver)

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
        home_page.input_into_search_box(search_val)
        home_page.click_search_button()
        assert "No results were found for your search" not in home_page.driver.page_source

class TestSignIn():
    '''Test sign in functionality.'''

    def test_proper_redirect(self,authentication_page):
        assert authentication_page.driver.current_url == 'http://automationpractice.com/index.php?controller=authentication&back=my-account'


class TestRegistration():
    '''Test registration process.'''

    @pytest.mark.parametrize('wrong_emails', [(' '),('wrong@.com'),('foo@bar'),])
    def test_try_create_an_account_with_invalid_email(self,registration_page,wrong_emails):
        '''Clicking "Create an account" with wrong email in text box should return an error.'''
        registration_page.input_into_create_an_account_email_box(wrong_emails)
        registration_page.click_create_an_account_button()
        assert  'class="alert alert-danger"' in registration_page.driver.page_source

    @pytest.mark.valid_register
    def test_try_create_an_account_with_valid_email(self,registration_page):
        '''Clicking "Create an account" with valid email.'''
        user_email = 'mp_user_{}@test.pl'.format(str(time.time())[-5:]) #creates email addres
        registration_page.input_into_create_an_account_email_box(user_email)
        registration_page.click_create_an_account_button()
        registration_page.wait_for_form()
        assert registration_page.driver.current_url == 'http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation'

    @pytest.mark.valid_register
    def test_try_register_valid_user(self,registration_page):
        '''Should register valid user.'''

        #YOUR PERSONAL INFORMATION
        registration_page.click_male_gender_button()
        registration_page.fill_first_name('Jan')
        registration_page.fill_last_name('Kowalski')
        registration_page.fill_password('qwerty')
        registration_page.select_date_of_birth('6','8','1992')
        registration_page.click_newsletter()
        registration_page.click_special_offers()

        #YOUR ADDRESS
        registration_page.fill_first_name_address('Jan')
        registration_page.fill_last_name_address('Kowalski')
        registration_page.fill_company_name_address('Unemployed')
        registration_page.fill_first_box_address('Johnson\'s street')
        registration_page.fill_second_box_address('Test Avenue 42')
        registration_page.fill_city_box_address('New York')
        registration_page.select_state_address('53')
        registration_page.fill_postal_code_box_address('02689')
        registration_page.select_country_address()
        registration_page.fill_additional_information_box_address('Lorem Ipsum Dolor Sit Amet.')
        registration_page.fill_home_phone_box_address('45 235 66 35')
        registration_page.fill_mobile_phone_box_address('123 456 789')
        registration_page.fill_alias_box_address('My address')

        registration_page.click_register_button()

        assert 'class="alert alert-danger"' not in registration_page.driver.page_source







