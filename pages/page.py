from selenium import webdriver
from pages import locators
import time

class BasePage():
    '''Base class to initialize in all page objects'''
    def __init__(self,driver):
        self.driver = driver

    def input_into_box(self, value, location):
        '''Input search values into box.'''
        element = self.driver.find_element(*location)
        element.clear()
        element.send_keys(value)

class HomePage(BasePage):
    '''Home page actions and methods.'''
    def __init__(self, driver):
        super(HomePage,self).__init__(driver)

    def click_cart(self):
        '''Opens shopping cart.'''
        element = self.driver.find_element(*locators.HomePage_locators.CART)
        element.click()

    def click_search_button(self):
        '''Clicks search button.'''
        element = self.driver.find_element(*locators.Common_locators.SEARCH_BUTTON)
        element.click()

    def click_sign_in_button(self):
        '''Clicks "sign in" button.'''
        element = self.driver.find_element(*locators.Common_locators.SIGN_IN)
        element.click()

    def cart_title_match(self):
        '''Verifies that title is "Order - My Store"'''
        return "Order - My Store" == self.driver.title


    def input_into_search_box(self,search_value):
        '''Input search values into search box.'''
        self.input_into_box(search_value,locators.Common_locators.SEARCH_BOX)

class AuthenticationPage(BasePage):

    def valid_email(self):
        return 'mp_user_{}@test.pl'.format(str(time.time())[-5:]) #creates email addres

    def click_create_an_account_button(self):
        '''Clicks "create an account" button'''
        element = self.driver.find_element(*locators.AuthenticationPage_locators.CREATE_ACCOUNT_BUTTON)
        element.click()

    def input_into_create_an_account_email_box(self, value):
        '''Input text into register "Email addres" box.'''
        self.input_into_box(value, locators.AuthenticationPage_locators.REGISTER_EMAIL_BOX)

    def start_creating_new_account(self, value):
        '''Input email address into proper box and clicks "Create an account" button.'''
        self.input_into_create_an_account_email_box(value)
        self.click_create_an_account_button()

    def fill_login_email_address(self,value):
        '''Fills "Email address" field in login section.'''
        self.input_into_box(value, locators.AuthenticationPage_locators.LOGIN_EMAIL_BOX)

    def fill_login_password_address(self,value):
        '''Fills "Password" field in login section.'''
        self.input_into_box(value, locators.AuthenticationPage_locators.LOGIN_PASSWORD_BOX)

    def click_sign_in_button(self):
        '''Clicks "Sign in" button in login section.'''
        element = self.driver.find_element(*locators.AuthenticationPage_locators.LOGIN_SUBMIT_BUTTON)
        element.click()

    def login(self, email, password):
        '''Login user.'''
        self.logout_if_logged_in()
        self.fill_login_email_address(email)
        self.fill_login_password_address(password)
        self.click_sign_in_button()

    def logout(self):
        '''Logout user.'''
        element = self.driver.find_element(*locators.Common_locators.SIGN_OUT)
        element.click()

    def is_logged(self):
        '''Check if user is logged in.'''
        return True if 'Sign out' in self.driver.page_source else False

    def logout_if_logged_in(self):
        '''Logout user if logged in.'''
        if self.is_logged():
            self.logout()

class ForgotPassword(AuthenticationPage):

    def fill_email(self, value):
        '''Fills "Email" field in retrieve password section.'''
        self.input_into_box(value, locators.ForgotPassword_locators.EMAIL_BOX)

    def click_retrieve_password_button(self):
        '''Clicks "Retrieve Password" button in retrieve password section.'''
        element = self.driver.find_element(*locators.ForgotPassword_locators.RETRIEVE_BUTTON)
        element.click()

    def forgot_password(self, value):
        '''Input email address and clicks retrieve button.'''
        self.fill_email(value)
        self.click_retrieve_password_button()

class RegistrationPage(AuthenticationPage):

    def wait_for_form(self):
        '''Wait for form to be fully loaded.'''
        from selenium.webdriver.support import expected_conditions as EC
        webdriver.support.ui.WebDriverWait(self.driver,10).until(EC.url_contains('#account-creation'))

    def click_male_gender_button(self):
        '''Clicks "Mr." radio button in a form.'''
        element = self.driver.find_element(*locators.RegisterPage_locators.GENDER_MALE_BUTTON)
        element.click()

    def click_female_gender_button(self):
        '''Clicks "Mr." radio button in a form.'''
        element = self.driver.find_element(*locators.RegisterPage_locators.GENDER_FEMALE_BUTTON)
        element.click()

    def fill_first_name(self, value):
        '''Fills "first name" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.FIRST_NAME_BOX)

    def fill_last_name(self, value):
        '''Fills "last name" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.LAST_NAME_BOX)

    def fill_password(self, value):
        '''Fills "password" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.PASSWORD_BOX)

    def select_date_of_birth(self,d,m,y):
        '''Select "Date of birth" d - day, m - month, y - year.'''
        from selenium.webdriver.support.ui import Select
        day = Select(self.driver.find_element(*locators.RegisterPage_locators.DATE_OF_BIRTH_DAY))
        day.select_by_value(d)
        month = Select(self.driver.find_element(*locators.RegisterPage_locators.DATE_OF_BIRTH_MONTH))
        month.select_by_value(m)
        year = Select(self.driver.find_element(*locators.RegisterPage_locators.DATE_OF_BIRTH_YEAR))
        year.select_by_value(y)

    def click_newsletter(self):
        '''Clicks newsletter button.'''
        element = self.driver.find_element(*locators.RegisterPage_locators.NEWSLETTER_BUTTON)
        element.click()

    def click_special_offers(self):
        '''Clicks special offers button.'''
        element = self.driver.find_element(*locators.RegisterPage_locators.SPECIAL_BUTTON)
        element.click()

    def fill_first_name_address(self, value):
        '''Fills "first name address" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.FIRST_NAME_ADDRESS_BOX)

    def fill_last_name_address(self, value):
        '''Fills "last name address" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.LAST_NAME_ADDRESS_BOX)

    def fill_company_name_address(self, value):
        '''Fills "company name address" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.COMPANY_NAME_ADDRESS_BOX)

    def fill_first_box_address(self, value):
        '''Fills "first address" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.ADDRESS_FIRST_BOX)

    def fill_second_box_address(self, value):
        '''Fills "second address" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.ADDRESS_SECOND_BOX)

    def fill_city_box_address(self, value):
        '''Fills "city" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.CITY_BOX)

    def select_state_address(self, state_number):
        '''Select "State" by number.'''
        from selenium.webdriver.support.ui import Select
        state = Select(self.driver.find_element(*locators.RegisterPage_locators.STATE))
        state.select_by_value(state_number)

    def fill_postal_code_box_address(self, value):
        '''Fills "postal code" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.POSTAL_CODE_BOX)

    def select_country_address(self):
        '''Select "Country". For now there's only one avaliable so it's auto selected by index.'''
        from selenium.webdriver.support.ui import Select
        state = Select(self.driver.find_element(*locators.RegisterPage_locators.COUNTRY))
        state.select_by_index(1)

    def fill_additional_information_box_address(self, value):
        '''Fills "Additional information" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.ADDITIONAL_INFO_AREA)

    def fill_home_phone_box_address(self, value):
        '''Fills "Home phone" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.HOME_PHONE_BOX)

    def fill_mobile_phone_box_address(self, value):
        '''Fills "Mobile phone" box.'''
        self.input_into_box(value, locators.RegisterPage_locators.MOBILE_PHONE_BOX)

    def fill_alias_box_address(self, value):
        '''Fills "Assign an address alias for future reference." box.'''
        self.input_into_box(value, locators.RegisterPage_locators.ALIAS_BOX)

    def click_register_button(self):
        '''Clicks register button.'''
        element = self.driver.find_element(*locators.RegisterPage_locators.REGISTER_SUBMIT_BUTTON)
        element.click()

    def valid_form_fill(self):
        #YOUR PERSONAL INFORMATION
        self.click_male_gender_button()
        self.fill_first_name('Jan')
        self.fill_last_name('Kowalski')
        self.fill_password('qwerty')
        self.select_date_of_birth('6','8','1992')
        self.click_newsletter()
        self.click_special_offers()

        #YOUR ADDRESS
        self.fill_first_name_address('Jan')
        self.fill_last_name_address('Kowalski')
        self.fill_company_name_address('Unemployed')
        self.fill_first_box_address('Johnson\'s street')
        self.fill_second_box_address('Test Avenue 42')
        self.fill_city_box_address('New York')
        self.select_state_address('53')
        self.fill_postal_code_box_address('02689')
        self.select_country_address()
        self.fill_additional_information_box_address('Lorem Ipsum Dolor Sit Amet.')
        self.fill_home_phone_box_address('45 235 66 35')
        self.fill_mobile_phone_box_address('123 456 789')
        self.fill_alias_box_address('My address')






