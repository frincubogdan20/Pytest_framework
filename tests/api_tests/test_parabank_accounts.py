import pytest
import xml.etree.ElementTree as ET

pytestmark = [pytest.mark.parabank, pytest.mark.api]

def test_get_accounts_for_customer(session, base_url, customer_id):
    resp = session.get(f"{base_url}/customers/{customer_id}/accounts")
    assert resp.status_code == 200
    root = ET.fromstring(resp.text)
    accounts = root.findall("account")
    assert len(accounts) > 0
    assert any(acc.find("customerId").text == str(customer_id) for acc in accounts)

def test_get_account_details(session, base_url, account_id):
    resp = session.get(f"{base_url}/accounts/{account_id}")
    assert resp.status_code == 200
    root = ET.fromstring(resp.text)
    assert root.find("id").text == str(account_id)
    assert root.find("balance") is not None
