"""User registration helpers."""


def register(
    username: str,
    password: str,
) -> dict:
    """
    Create a demo user representation.
    """

    if not username.strip():
        raise ValueError("Username cannot be empty")

    if len(password) < 6:
        raise ValueError(
            "Password must contain at least 6 characters"
        )

    return {
        "username": username.strip(),
        "registered": True,
    }