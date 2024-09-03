import attr
from attr import attrib, attrs
import pytest

@pytest.mark.usefixtures('db_get')
@attrs
class User:
    password = attrib()
    email = attrib()
