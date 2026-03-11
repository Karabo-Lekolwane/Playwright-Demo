import pytest

from conftest import test_data
from pages.login_page import Login
from pages.checkout_page import Checkout

product = "Digital SLR Camera"


class TestCartAndCheckout:
    def test_add_to_cart_and_checkout(self, page, registered_user):
        assert registered_user.get("email"), (
            "No registered user found. Run Part 1 first."
        )

        email = registered_user["email"]
        password = registered_user["password"]

        login_page = Login(page)
        login_page.navigate()
        login_page.login(registered_user["email"], registered_user["password"])
        login_page.assert_logged_in(registered_user["email"])

        cart_page = Checkout(page)
        cart_page.navigate_to_product()

        cart_page.navigate_to_product()
        cart_page.select_product()
        cart_page.add_to_cart()

        cart_page.open_cart()
        cart_page.assert_cart_contains(product_name=product, quantity=1)

        cart_page.proceed_to_checkout()
        cart_page.fill_billing_address(test_data)
        cart_page.shipping_address()
        cart_page.shipping_method()
        cart_page.fill_payment_method()
        cart_page.fill_payment_info(test_data)
        cart_page.confirm_order()

        cart_page.assert_order_confirmed()
