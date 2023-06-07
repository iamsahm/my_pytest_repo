from lib.greet import *

def test_greet():
    result = greet('Sam')
    assert result == 'Hello, Sam!'