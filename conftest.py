import pytest
import requests
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def heroku_base_url() -> str:
    return "https://the-internet.herokuapp.com"

@pytest.fixture(scope="session")
def academy_base_url() -> str:
    return "https://academybugs.com"

@pytest.fixture(scope="session")
def base_url():
    return "https://parabank.parasoft.com/parabank/services/bank"

@pytest.fixture(scope="session")
def demo_user():
    return {"username": "john", "password": "demo"}

@pytest.fixture(scope="session")
def customer_id():
    # ParaBank demo user "john" is id 12212
    return 12212

@pytest.fixture(scope="session")
def account_id():
    # Account id for user "John" is 13344
    return 13344

@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    return s

@pytest.fixture(scope="session")
def browser():
    """Launch a Chromium browser (headed or headless)."""
    with sync_playwright() as pw:
        # This is where your line goes
        browser = pw.chromium.launch(
            headless=False,  # Change to True for headless
            args=[
                "--no-sandbox",
                "--disable-gpu"
            ]
        )
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    """Return a new page object for each test."""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    yield page
    context.close()