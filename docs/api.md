# API

## Authentication

`register_user(username, password, users)` registers a user in an in-memory
mapping.

`authenticate(username, password, users)` checks the supplied credentials.

## Payment

`calculate_total(amount, tax_rate)` calculates an amount including tax.
