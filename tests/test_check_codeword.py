from lib.check_codeword import *
    

def test_code_word():
    result = check_codeword('horse')
    assert result == "Correct! Come in."
    result = check_codeword('house')
    assert result == "Close, but nope."
    result = check_codeword('check')
    assert result == "WRONG!"