import pytest

def test_login_creds(db_get):
    print(db_get.email, db_get.password)