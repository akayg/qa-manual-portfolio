# test_markers_demo.py

import pytest

@pytest.mark.smoke
def test_login():
    assert "user" in "user_login_success"

@pytest.mark.regression
def test_profile_update():
    assert 1 + 1 == 2

@pytest.mark.api
def test_api_data():
    assert {"status": "ok"}["status"] == "ok"
