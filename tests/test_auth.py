from src.auth.login import login
from src.auth.register import register


def test_login_success():
    assert login("admin", "admin123") is True


def test_login_failure():
    assert login("admin", "wrong") is False


def test_register():
    user = register(
        "student",
        "password123",
    )

    assert user["username"] == "student"
    assert user["registered"] is True