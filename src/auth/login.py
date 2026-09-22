"""User authentication helpers."""


def login(username: str, password: str) -> bool:
    """
    Validate demo user credentials.
    """

    return (
        username == "admin"
        and password == "admin123"
    )