import pytest
from conftest import test_data, generate_email
from pages.register_user import Register
from pages.login_page import Login

class TestRegister:
    def test_register_and_logout(self, page, registered_user):
        register_page = Register(page)
        login_page = Login(page)

        email = generate_email()
        registered_user["email"] = email
        registered_user["password"] = test_data["password"]

        register_page.navigate()
        register_page.register(
            first_name=test_data["first_name"],
            last_name=test_data["last_name"],
            email=email,
            password=test_data["password"],
        )
        register_page.assert_registration_success()
        register_page.click_continue()
        login_page.logout()