import nose
from tmp.my_range import my_range

def test_my_range():
    assert my_range(5) == range(5)
    assert my_range(1, 10) == range(1, 10)
    assert my_range(1, 10, 2) == range(1, 10, 2)
    assert my_range(-10, 10, 2) == range(-10, 10, 2)
#     assert my_range() == range()

if __name__ == '__main__':
    nose.runmodule()