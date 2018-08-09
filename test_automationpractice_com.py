from selenium import webdriver
from pages import page
import pytest
import time

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

class TestLogin():
    '''Test sign in functionality.'''

    def test_proper_redirect(self,authentication_page):
        assert authentication_page.driver.current_url == 'http://automationpractice.com/index.php?controller=authentication&back=my-account'

    def test_valid_login(self, authentication_page):
        authentication_page.login('test_test@test.test', 'qwerty')
        assert "Sign out" and "Welcome to your account. Here you can manage all of your personal information and orders." in authentication_page.driver.page_source

    def test_invaild_password(self, authentication_page):
        authentication_page.login('test_test@test.test', 'wrong_pass')
        assert "Authentication failed." in authentication_page.driver.page_source

    def test_invaild_email(self, authentication_page):
        authentication_page.login('wrong@wrong.wrong', 'qwerty')
        assert "Authentication failed." in authentication_page.driver.page_source

    def test_empty_email(self, authentication_page):
        authentication_page.login('', 'wrong_pass')
        assert "An email address required." in authentication_page.driver.page_source

class TestRegistration():
    '''Test registration process.'''

    @pytest.mark.parametrize('wrong_emails', [(' '),('wrong@.com'),('foo@bar'),])
    def test_try_create_an_account_with_invalid_email(self,registration_page,wrong_emails):
        '''Clicking "Create an account" with wrong email in text box should return an error.'''
        registration_page.start_creating_new_account(wrong_emails)
        assert  'class="alert alert-danger"' in registration_page.driver.page_source

    @pytest.mark.valid_register
    def test_try_create_an_account_with_valid_email(self,registration_page):
        '''Clicking "Create an account" with valid email.'''
        registration_page.start_creating_new_account(registration_page.valid_email())
        registration_page.wait_for_form()
        assert registration_page.driver.current_url == 'http://automationpractice.com/index.php?controller=authentication&back=my-account#account-creation'

    @pytest.mark.valid_register
    def test_try_register_valid_user(self,registration_page):
        '''Should register valid user.'''

        registration_page.start_creating_new_account(registration_page.valid_email())
        registration_page.wait_for_form()
        registration_page.valid_form_fill()
        registration_page.click_register_button()

        assert 'class="alert alert-danger"' not in registration_page.driver.page_source

    @pytest.mark.invalid_register
    def test_try_register_with_no_values(self, registration_page):
        registration_page.logout_if_logged_in()
        registration_page.start_creating_new_account("vailid@email.com")
        registration_page.wait_for_form()
        registration_page.click_register_button()
        assert  'class="alert alert-danger"' in registration_page.driver.page_source








