from selenium.webdriver.common.by import By


class CommonLocators:
    LOGIN_LINK = (By.XPATH, "//li[@class='login-button']")
    LOGIN_FRAME = (By.XPATH, "//div[@class = 'modal-dialog modal-cm']")
    USER_MENU = (By.XPATH, "//a[@id='nav-username']/span[@class='navbar-profile-label ng-binding']")
    USER_MENU_API_KEYS = (By.XPATH, "//a[@href='/cryptopian/api-keys']")


class MainPageLocators:
    MAIN_TABLE = (By.XPATH, "//div[@class='section overview-section']")


class LoginModalLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-login btn-lg btn-block']")


class ApiPageLocators:
    API_FORM = (By.XPATH, "//form[@class='col-md-12 item-key-wrapper ng-pristine ng-valid ng-scope']")
    API_KEY_VALUE_INPUT = (By.XPATH, "//input[@id='key-value-0']")