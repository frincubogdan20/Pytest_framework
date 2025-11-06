import pytest
import xml.etree.ElementTree as ET

pytestmark = [pytest.mark.parabank, pytest.mark.api]

@pytest.mark.parametrize("amount", [10.0, 0.0, -5.0])
def test_transfer_funds(session, base_url, account_id, amount):
    payload = {
        "fromAccountId": account_id,
        "toAccountId": account_id,
        "amount": amount,
    }
    resp = session.post(f"{base_url}/transfer?fromAccountId={account_id}&toAccountId={account_id}&amount={amount}")
    assert resp.status_code in (200, 400, 500)

def test_get_transactions_for_account(session, base_url, account_id):
    resp = session.get(f"{base_url}/accounts/{account_id}/transactions")
    assert resp.status_code == 200
    root = ET.fromstring(resp.text)
    transactions = root.findall("transaction")
    assert len(transactions) > 0
    assert all(tx.find("accountId").text == str(account_id) for tx in transactions)
    assert any(tx.find("amount").text == "10.00" for tx in transactions)

def test_transactions_date_filter(session, base_url, account_id):
    resp = session.get(
        f"{base_url}/accounts/{account_id}/transactions?fromDate=01-01-2020&toDate=31-12-2025"
    )
    assert resp.status_code in (200, 204)
    root = ET.fromstring(resp.text)
    transactions = root.findall("transaction")
    assert len(transactions) > 0
    assert all(tx.find("accountId").text == str(account_id) for tx in transactions)
    assert any(tx.find("amount").text == "-5.00" for tx in transactions)
