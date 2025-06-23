# conftest.py

import pytest

@pytest.fixture
def sample_user():
    return {
        "username": "test_user",
        "email": "test@example.com",
        "role": "admin"
    }
