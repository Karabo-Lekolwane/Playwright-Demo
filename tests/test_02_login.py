import pytest
from pages.login_page import Login

class TestLogin:
    @pytest.mark.parametrize(
        "credentials, expected_to_fail",
        [
            pytest.param("valid", False, id="valid_login"),

            pytest.param(
                ("testemail@test.com", "testPassword!"),
                True,
                marks=pytest.mark.xfail(reason="Testing invalid credentials"),
                id="invalid_login"
            )
        ]
    )
    def test_login_with_credentials(self, page, registered_user, credentials, expected_to_fail):
        login_page = Login(page)
        login_page.navigate()

        if credentials == "valid":

            assert registered_user.get("email"), "No registered user found from Part 1."
            email = registered_user["email"]
            password = registered_user["password"]
        else:

            email, password = credentials

        login_page.login(email, password)

        if expected_to_fail:

            error_locator = page.locator("div.validation-summary-errors")
            assert error_locator.is_visible(), "Error message should be visible"

            if email == "wrong_user@test.com":
                login_page.assert_logged_in(email)
        else:

            login_page.assert_logged_in(email)