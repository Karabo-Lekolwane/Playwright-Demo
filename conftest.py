import pytest
import uuid
from playwright.sync_api import sync_playwright

test_data = {
    "first_name": "Barbara",
    "last_name": "Gordon",
    "password": "Tosca1234!",
    "country": "Austria",
    "city": "Vienna",
    "address": "Vienna Street",
    "zip": "1234",
    "phone": "001122334455",
    "card_type": "Visa",
    "cardholder": "Barbara Gordon",
    "card_number": "4485564059489345",
    "expiry_month": "04",
    "expiry_year": "2030",
    "cvv": "123",
}

@pytest.fixture(scope="session")
def registered_user():
    return {}

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=800)
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    yield page


def generate_email():
    return f"test_user_{uuid.uuid4().hex[:8]}@example.com"