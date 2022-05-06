import pytest

from app import app


def test_index(client):
    resp = client.get("/")

    assert b"Welcome to Strengthy" in resp.data


# horrible name
def test_workout_create_notloggedin(client):
    resp = client.get("/workout/create", follow_redirects=True)

    # Make sure redirect worked
    assert resp.request.path == "/login"


def test_home_notloggedin(client):
    resp = client.get("/home", follow_redirects=True)

    # Make sure redirect worked
    assert resp.request.path == "/login"
