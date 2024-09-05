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
        user_mail = f"{user.username}"
        user_password = f"{user.password}"
        return user_mail, user_password
    else:
        db_manager.add_user(DBCreds.USER_MAIL, DBCreds.USER_PWD, DBCreds.API_KEY)


@pytest.fixture
def db_get():
    user_mail, user_password = user_init()
    user = User(email=user_mail, password=user_password)
    yield user

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default='en', help="Choose language, default - 'en'")


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_argument('--start-maximized')
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()