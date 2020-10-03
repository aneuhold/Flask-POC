def func(x):
    return x + 1

import pytest
from hello import create_app

@pytest.fixture
def test_client():
    """
    Builds a client which can be used to test endpoints on the Flask server.
    """

def test_answer():
    assert func(3) == 5