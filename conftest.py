import pytest
import requests

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
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "screen": {"width": 1920, "height": 1080},
    }