import pytest
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/game")
    assert_response(resp)

    # test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp, status="404")
