from selenium.webdriver.common.by import By

class HomePage_locators():
    LOGO = (By.XPATH, '//img[@alt="My Store"]')
    CART = (By.XPATH, '//a[@title="View my shopping cart"]')

class Common_locators():
    SEARCH_BUTTON = (By.XPATH, '//button[@name="submit_search"]')
    SEARCH_BOX = (By.XPATH, '//input[@name="search_query"]')


