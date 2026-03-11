from playwright.sync_api import Page, expect


class Register:
    URL = "https://demowebshop.tricentis.com/register"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def register(self, first_name: str, last_name: str, email: str, password: str):

        self.page.get_by_role("radio", name="Female").check()
        self.page.get_by_role("textbox", name="First name:").fill(first_name)
        self.page.get_by_role("textbox", name="Last name:").fill(last_name)
        self.page.get_by_role("textbox", name="Email:").fill(email)
        self.page.get_by_role("textbox", name="Password:", exact=True).fill(password)
        self.page.get_by_role("textbox", name="Confirm password:").fill(password)
        self.page.get_by_role("button", name="Register").click()

    def click_continue(self):
        self.page.get_by_role("button", name="Continue").click()

    def assert_registration_success(self):
        success = self.page.locator(".result")
        expect(success).to_be_visible()
        expect(success).to_contain_text("Your registration completed")
