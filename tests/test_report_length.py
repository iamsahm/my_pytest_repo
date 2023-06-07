from lib.report_length import *

def test_report_length():
    result = report_length('sam')
    assert result == 'This string was 3 characters long.'