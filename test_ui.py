from conftest import get_creds_from_db
from pages.api_key_page import ApiKeyPage
from pages.main_page import MainPage


class TestUserCanGetApi:
    def test_login(self, driver, get_creds_from_db):
        """
        1. Go to the main page
        2. Check that the main table is appeared
        3. Check that the login button is visible
        4. Click on the login button
        5. Check that the e-mail and password boxes are visible
        6. Input creds in boxes
        7. Click the login button
        8. Check that the username is visible on the top right of the main table
        """
        link = "https://www.cryptocompare.com/"
        page = MainPage(driver, link)
        page.open()
        page.main_page_opened()
        page.go_to_login_page()
        page.login(get_creds_from_db.email, get_creds_from_db.password)

    def test_api_key_value(self, driver, get_creds_from_db):
        """
        1. Click on the user menu button
        2. Check that the API key button is visible
        3. Click on the API key button
        4. Check that the form with API keys is visible
        5. Check that the input box with API key is visible
        6. Check that common API key type is "password"
        7. Check that the API key in the box matches the one in DB
        """
        page = MainPage(driver, driver.current_url)
        page.open_api_keys_page()
        page = ApiKeyPage(driver, driver.current_url)
        page.api_key_page_opened()
        page.get_api_key_value(get_creds_from_db.api_key)
