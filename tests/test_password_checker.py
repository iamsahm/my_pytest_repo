import pytest
from lib.password_checker import *

# check passwords longer than 8 return True
def test_long():
    check = PasswordChecker()
    result = check.check('longpasswordislong')
    assert result == True

# check passwords of exactly length 8 return True
def test_long():
    check = PasswordChecker()
    result = check.check('password')
    assert result == True
# raise exception for passwords less than 8
def test_lessthan():
    check = PasswordChecker()
    with pytest.raises(Exception) as err:
        check.check('four')
    error_message = str(err.value)
    assert error_message == "Invalid password, must be 8+ characters."