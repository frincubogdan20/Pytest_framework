import pytest
import xml.etree.ElementTree as ET

pytestmark = [pytest.mark.parabank, pytest.mark.api]

def test_get_customer_info(session, base_url, customer_id):
    resp = session.get(f"{base_url}/customers/{customer_id}")
    assert resp.status_code == 200
    root = ET.fromstring(resp.text)
    assert root.find("id").text == str(customer_id)

def test_get_customer_invalid(session, base_url):
    resp = session.get(f"{base_url}/customers/9999999")
    assert resp.status_code in (404, 400)
