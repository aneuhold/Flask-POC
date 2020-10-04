import pytest
import server


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


@pytest.fixture
def test_client():
    """
    Builds a client which can be used to test endpoints on the Flask server.
    """

    server.app.config['TESTING'] = True
    testingClient = server.app.test_client()

    context = server.app.app_context()
    context.push()

    yield testingClient

    context.pop()


def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
