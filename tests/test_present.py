import pytest
from lib.present import *


def test_wrap_and_unwrap():
    present = Present()
    present.wrap(3)
    result = present.unwrap()
    assert result == 3

def test_unwrap_before():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == 'No contents have been wrapped.'

def test_wrap_twice():
    present = Present()
    present.wrap(3)
    with pytest.raises(Exception) as e:
        present.wrap(3)
    message = str(e.value)
    assert message == "A contents has already been wrapped."