"""Test data for SauceDemo. Keeps credentials and sample checkout data in one place."""
USERS = {
    "standard_user": {"username": "standard_user", "password": "secret_sauce"},
    "locked_out_user": {"username": "locked_out_user", "password": "secret_sauce"},
    "problem_user": {"username": "problem_user", "password": "secret_sauce"},
}

CHECKOUT_USER = {
    "first_name": "Jane",
    "last_name": "Doe",
    "postal_code": "12345",
}
