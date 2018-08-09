import pytest
from selenium import webdriver
from pages import page

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

@pytest.fixture(scope='function')
def registration_page(set_driver):
    '''Return RegistrationPage object.'''
    set_driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
    return page.RegistrationPage(set_driver)

if __name__ == '__main__':
    main()
