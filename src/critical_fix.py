"""Critical validation fix."""


def is_valid_amount(amount: float) -> bool:
    """Return True only for positive payment amounts."""

    return amount > 0