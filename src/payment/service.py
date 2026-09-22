"""Small payment module for the feature/add-payment branch exercise."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


def calculate_total(amount: Decimal, tax_rate: Decimal = Decimal("0.20")) -> Decimal:
    """Return amount plus tax, rounded to two decimal places."""
    if amount < 0:
        raise ValueError("Amount must not be negative")
    total = amount * (Decimal("1.00") + tax_rate)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
