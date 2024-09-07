from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(10)

    def open(self):
        self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.driver, 30, 0.3).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_displayed(self, how, what):
        try:
            WebDriverWait(self.driver, 30, 0.3).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_clickable(self, how, what):
        try:
            WebDriverWait(self.driver, 30, 0.3).until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            return False

        return True

    # def navigate_to(self, what):
    #     WebDriverWait(self.driver, 30, 0.3).until(EC.element_to_be_clickable((By.XPATH, what)))
    #     self.driver.find_element(By.XPATH, what).click()
