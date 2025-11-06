import pytest
import xml.etree.ElementTree as ET

pytestmark = [pytest.mark.parabank, pytest.mark.api]

def test_clean_db(session, base_url):
    clean_db = f"{base_url}/cleanDB"
    resp = session.post(clean_db)
    assert resp.status_code in (204, 403, 500)

def test_initialize_db(session, base_url):
    init_db = f"{base_url}/initializeDB"
    resp = session.post(init_db)
    assert resp.status_code in (204, 403, 500)
