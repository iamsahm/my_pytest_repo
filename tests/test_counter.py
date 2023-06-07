from lib.counter import *

def test_counter():
    counter = Counter()
    counter.add(1)
    result = counter.report()
    assert result == "Counted to 1 so far."
    counter.add(3)