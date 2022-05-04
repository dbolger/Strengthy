from app import create_app

def test_home_page():
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """

    flask_app = create_app('flask_test.cfg')

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Welcome to Strengthy" in response.data
        assert b"Strengthy is an open source fitness tracking applicatio that helps users meet their fitness goals." in response.data
        assert b"To get started, Sign Up to create an account." in response.data
