
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
singleton = Singleton()
another_singleton = Singleton()
print('singleton is another_singleton', singleton is another_singleton)

singleton.only_one_var = "I'm only one var"
print(another_singleton.only_one_var)

class Child(Singleton):
    pass

child = Child()
print('child is singleton', child is singleton)
print('child.only_one_var', child.only_one_var)