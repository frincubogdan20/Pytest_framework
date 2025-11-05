import pytest

@pytest.fixture(scope="session")
def heroku_base_url() -> str:
    return "https://the-internet.herokuapp.com"

@pytest.fixture(scope="session")
def academy_base_url() -> str:
    return "https://academybugs.com"