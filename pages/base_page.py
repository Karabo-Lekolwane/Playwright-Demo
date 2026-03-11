from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def wait_for_element(self, selector: str, state: str = "visible"):
        return self.page.wait_for_selector(selector, state=state)

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    def get_text(self, selector: str) -> str:
        element = self.page.locator(selector).first
        return element.text_content() or ""

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
