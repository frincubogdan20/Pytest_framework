import pytest
import xml.etree.ElementTree as ET

pytestmark = [pytest.mark.parabank, pytest.mark.api]

def test_login_valid(session, base_url, demo_user):
    resp = session.get(f"{base_url}/login/{demo_user['username']}/{demo_user['password']}")
    assert resp.status_code in (200, 302), f"Unexpected status: {resp.status_code}"
    root = ET.fromstring(resp.text)
    assert root.find("firstName").text == "John"
    assert root.find("lastName").text == "Smith"

@pytest.mark.parametrize("user,pw", [
    ("invalid", "demo"),
    ("john", "wrongpass"),
])
def test_login_invalid(session, base_url, user, pw):
    resp = session.get(f"{base_url}/login/{user}/{pw}")
    assert resp.status_code in (400, 401, 500), f"Unexpected status: {resp.status_code}"
