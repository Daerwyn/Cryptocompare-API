from pages.base_page import BasePage
from pages.locators import ApiPageLocators


class ApiKeyPage(BasePage):
    def api_key_page_opened(self):
        assert self.is_element_present(*ApiPageLocators.API_FORM), "Api form is not present"

    def get_api_key_value(self, api_key):
        self.is_element_present(*ApiPageLocators.API_KEY_VALUE_INPUT)
        api_key_value = self.driver.find_element(*ApiPageLocators.API_KEY_VALUE_INPUT).get_attribute("value")
        assert api_key_value == api_key
