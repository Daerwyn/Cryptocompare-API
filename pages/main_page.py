import time

from pages.base_page import BasePage

from pages.locators import MainPageLocators, CommonLocators, LoginModalLocators


class MainPage(BasePage):
    def main_page_opened(self):
        assert self.is_element_present(*MainPageLocators.MAIN_TABLE), "Main table is not present."
        assert self.is_element_present(*CommonLocators.LOGIN_LINK), "Login link is not present."

    def go_to_login_page(self):
        login_link = self.driver.find_element(*CommonLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_displayed(*LoginModalLocators.EMAIL_INPUT), "E-mail input is not present."
        assert self.is_element_displayed(*LoginModalLocators.PASSWORD_INPUT), "Password input is not present."

    def login(self, user, password):
        email_input = self.driver.find_element(*LoginModalLocators.EMAIL_INPUT)
        password_input = self.driver.find_element(*LoginModalLocators.PASSWORD_INPUT)
        email_input.send_keys(user)
        password_input.send_keys(password)
        self.driver.find_element(*LoginModalLocators.LOGIN_BUTTON).click()
        self.is_element_displayed(*CommonLocators.USER_MENU)
        assert self.driver.find_element(*CommonLocators.USER_MENU).text == user.split("@")[
            0], "Username is not displayed"

    def open_api_keys_page(self):
        user_menu_button = self.driver.find_element(*CommonLocators.USER_MENU)
        user_menu_button.click()
        self.is_element_clickable(*CommonLocators.USER_MENU_API_KEYS)
        user_menu_api_key_button = self.driver.find_element(*CommonLocators.USER_MENU_API_KEYS)
        user_menu_api_key_button.click()
        time.sleep(2)
