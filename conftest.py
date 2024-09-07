import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from models.users import User
from DBManagment.DB_creds import DBCreds
from DBManagment.DB_session import DBManager

db_manager = DBManager('mysql+mysqldb://root:12344321@127.0.0.1:3307/Cryptocompare')
db_manager.create_table()


def user_init():
    user = db_manager.get_user(DBCreds.USER_MAIL)
    if user:
        pass
    else:
        db_manager.add_user(DBCreds.USER_MAIL, DBCreds.USER_PWD, DBCreds.API_KEY)
        user = db_manager.get_user(DBCreds.USER_MAIL)
    user_mail = f"{user.username}"
    user_password = f"{user.password}"
    api_creds = db_manager.get_api_key(DBCreds.USER_MAIL)
    api_key = f"{api_creds.api_key}"
    return user_mail, user_password, api_key



@pytest.fixture
def get_creds_from_db():
    user_mail, user_password, api_key = user_init()
    user = User(email=user_mail, password=user_password, api_key=api_key)
    yield user


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en', help="Choose language, default - 'en'")


@pytest.fixture(scope='class')
def driver(request):
    options = Options()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()
