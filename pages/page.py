from pages import locators
from pages import elements

class BasePage():
    '''Base class to initialize in all page objects'''
    def __init__(self,driver):
        self.driver = driver

class HomePage(BasePage):
    '''Home page actions and methods.'''
    def __init__(self, driver):
        super(HomePage,self).__init__(driver)
        self.search_value = None

    def click_cart(self):
        '''Opens shopping cart.'''
        element = self.driver.find_element(*locators.HomePage_locators.CART)
        element.click()

    def click_search_button(self):
        '''Clicks search button.'''
        element = self.driver.find_element(*locators.Common_locators.SEARCH_BUTTON)
        element.click()

    def cart_title_match(self):
        '''Verifies that title is "Order - My Store"'''
        return "Order - My Store" == self.driver.title

    def search_any_results(self):
        '''Verifies that there are some search results'''
        return "No results were found for your search" not in self.driver.page_source

    def input_into_search_box(self):
        '''Input search values into search box.'''
        element = self.driver.find_element(*locators.Common_locators.SEARCH_BOX)
        element.clear()
        element.send_keys(self.search_value)



