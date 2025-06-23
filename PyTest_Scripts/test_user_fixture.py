# test_user_fixture.py

import pytest

# This fixture returns a sample user dictionary
@pytest.fixture
def user_data():
    return {
        "username": "admin",
        "password": "admin@123"
    }

def test_username(user_data):
    assert user_data["username"] == "admin"

def test_password_length(user_data):
    assert len(user_data["password"]) >= 8


@pytest.fixture
def connect_db():
    print("\n[Setup] Connecting to DB")
    yield "DB_CONNECTION_OBJECT"
    print("[Teardown] Closing DB connection")

def test_db_query(connect_db):
    assert connect_db == "DB_CONNECTION_OBJECT"
