from playwright.sync_api import Page, expect


class Login:
    URL = "https://demowebshop.tricentis.com/login"

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.page.get_by_role("textbox", name="Email:").fill(email)
        self.page.get_by_role("textbox", name="Password:").fill(password)
        self.page.get_by_role("button", name="Log in").click()

    def logout(self):
        self.page.get_by_role("link", name="Log out").click()

    def assert_logged_in(self, email: str):
        account_link = self.page.locator(f".account[href='/customer/info']").filter(has_text=email)
        expect(account_link).to_be_visible()

    def assert_logged_out(self):
        expect(self.page.get_by_role("link", name="Log in")).to_be_visible()
        expect(self.page.get_by_role("link", name="Log out")).not_to_be_visible()
