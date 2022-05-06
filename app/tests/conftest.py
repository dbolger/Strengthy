import pytest

from app import app
from tables import User


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="module")
def new_user():
    user = User("gymdude99", "bench400soon!", "gymdude99@gmail.com")
    return user
