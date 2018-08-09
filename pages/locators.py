from selenium.webdriver.common.by import By

class HomePage_locators():
    LOGO = (By.XPATH, '//img[@alt="My Store"]')
    CART = (By.XPATH, '//a[@title="View my shopping cart"]')

class Common_locators():
    SEARCH_BUTTON = (By.XPATH, '//button[@name="submit_search"]')
    SEARCH_BOX = (By.XPATH, '//input[@name="search_query"]')
    SIGN_IN = (By.XPATH, '//a[@class="login"]')
    SIGN_OUT = (By.XPATH, '//a[@class="logout"]')

class AuthenticationPage_locators():
    REGISTER_EMAIL_BOX = (By.XPATH, '//input[@name="email_create"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[@name="SubmitCreate"]')

    LOGIN_EMAIL_BOX = (By.XPATH, '//input[@name="email"]')
    LOGIN_PASSWORD_BOX = (By.XPATH, '//input[@name="passwd"]')

    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[@name="SubmitLogin"]')

    FORGOT_PASSWORD = (By.XPATH, '//a[@title="Recover your forgotten password"]')

class ForgotPassword_locators():
    EMAIL_BOX = (By.XPATH,'//input[@name="email"]')
    RETRIEVE_BUTTON = (By.XPATH,'//button[@class="btn btn-default button button-medium"][@type="submit"]')

class RegisterPage_locators():
    GENDER_MALE_BUTTON = (By.XPATH, '//input[@name="id_gender"][@value="1"]')
    GENDER_FEMALE_BUTTON = (By.XPATH, '//input[@name="id_gender"][@value="2"]')
    FIRST_NAME_BOX = (By.XPATH, '//input[@name="customer_firstname"]')
    LAST_NAME_BOX = (By.XPATH, '//input[@name="customer_lastname"]')
    EMAIL_BOX = (By.XPATH,'//input[@name="email"]')
    PASSWORD_BOX = (By.XPATH, '//input[@name="passwd"]')

    DATE_OF_BIRTH_DAY = (By.XPATH, '//select[@name="days"]')
    DATE_OF_BIRTH_MONTH = (By.XPATH, '//select[@name="months"]')
    DATE_OF_BIRTH_YEAR = (By.XPATH, '//select[@name="years"]')

    NEWSLETTER_BUTTON = (By.XPATH,'//input[@name="newsletter"]')
    SPECIAL_BUTTON = (By.XPATH,'//input[@name="optin"]')

    FIRST_NAME_ADDRESS_BOX = (By.XPATH,'//input[@name="firstname"]')
    LAST_NAME_ADDRESS_BOX = (By.XPATH,'//input[@name="lastname"]')
    COMPANY_NAME_ADDRESS_BOX = (By.XPATH,'//input[@name="company"]')
    ADDRESS_FIRST_BOX = (By.XPATH,'//input[@name="address1"]')
    ADDRESS_SECOND_BOX = (By.XPATH,'//input[@name="address2"]')
    CITY_BOX = (By.XPATH,'//input[@name="city"]')
    STATE = (By.XPATH, '//select[@name="id_state"]')
    POSTAL_CODE_BOX = (By.XPATH,'//input[@name="postcode"]')
    COUNTRY = (By.XPATH, '//select[@name="id_country"]')
    ADDITIONAL_INFO_AREA = (By.XPATH,'//textarea[@name="other"]')
    HOME_PHONE_BOX = (By.XPATH,'//input[@name="phone"]')
    MOBILE_PHONE_BOX = (By.XPATH,'//input[@name="phone_mobile"]')
    ALIAS_BOX = (By.XPATH,'//input[@name="alias"]')

    REGISTER_SUBMIT_BUTTON = (By.XPATH, '//button[@name="submitAccount"]')




