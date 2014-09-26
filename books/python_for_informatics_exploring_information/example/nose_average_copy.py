import nose

def average(lst):
    return sum(lst) / float(len(lst))

def test_average():
    l = range(10)
    assert average(l) == 4.5
    assert 0 < average(l) < 9

if __name__ == '__main__':
    nose.runmodule()