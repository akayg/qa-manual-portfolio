# test_user_shared.py

def test_username(sample_user):
    assert sample_user["username"] == "test_user"

def test_email(sample_user):
    assert "@" in sample_user["email"]

def test_role(sample_user):
    assert sample_user["role"] == "admin"
