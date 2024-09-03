from attr import attrib, attrs


@attrs
class User:
    password = attrib()
    email = attrib()
