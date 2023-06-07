from lib.gratitudes import *
def test_gratitudes():
    gratitude = Gratitudes()
    gratitude.add('farts')
    gratitude.add('boobies')
    gratitude.add('buttcracks')
    
    result = gratitude.format()
    assert result == "Be grateful for: farts, boobies, buttcracks"