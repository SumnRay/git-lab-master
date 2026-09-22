from decimal import Decimal

from src.payment import calculate_total


def test_calculate_total():
    assert calculate_total(Decimal("100.00")) == Decimal("120.00")
