from lib.string_builder import *
def test_string_builder():
    my_string = StringBuilder()
    my_string.add('this comes first')
    result = my_string.size()
    assert result == len('this comes first')
    result = my_string.output()
    assert result == 'this comes first'