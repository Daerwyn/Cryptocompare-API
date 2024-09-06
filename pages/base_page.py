from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 30, 0.3)

    def open(self):
        self.driver.get(self.url)

    def _is_element_present(self, how, what):
        try:
            self.driver.wait.until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True


