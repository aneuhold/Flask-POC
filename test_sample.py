import pytest
from hello import create_app


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


@pytest.fixture
def test_client():
    """
    Builds a client which can be used to test endpoints on the Flask server.
    """

    app = create_app('flask_test.cfg')

    testingClient = app.test_client()

    context = app.app_context()
    context.push()

    yield testingClient

    context.pop()
