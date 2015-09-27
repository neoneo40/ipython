class Borg(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class Child(Borg):
    pass


class AnotherChild(Borg):
    _shared_state = {}

borg = Borg()
another_borg = Borg()
print borg is another_borg

child = Child()
borg.only_one_var = "I'm the only one var"
print child.only_one_var

another_child = AnotherChild()
print another_child.only_one_var