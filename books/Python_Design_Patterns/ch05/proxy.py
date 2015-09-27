# -*- coding: utf-8

from abc import ABCMeta, abstractmethod
import random

class AbstractSubject(object):
    '''실제와 프록시 객체에 대한 일반적인 인터페이스'''

    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, reverse=False):
        pass


class RealSubject(AbstractSubject):
    '''인스턴스화 하는데 많은 시간과 메모리를 차지하는 커다란 객체에 대한 클래스'''

    def __init__(self):
        self.digits = []

        for i in xrange(1000):
            self.digits.append(random.random())

    def sort(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()


class Proxy(AbstractSubject):
    '''RealSubject와 동일한 인터페이스를 갖는 프록시'''
    reference_count = 0

    def __init__(self):
        '''기존에 생성된 것이 있으면 캐시 해 놓고, 없다면 생성하는 생성자'''
        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealSubject()
            print 'Created new object'
        else:
            print 'Using cached object'

        self.__class__.reference_count += 1
        print 'Count of references = ', self.__class__.reference_count

    def sort(self, reverse=False):
        '''인자는 프록시에 의해 기록된다.'''
        print 'Called sort method with args:'
        print locals().items()

        self.__class__.cached_object.sort(reverse=reverse)

    def __del__(self):
        '''객체에 대한 참조를 감소시킴. 만약 참조가 0이 되면 객체를 삭제한다.'''
        self.__class__.reference_count -= 1

        if self.__class__.reference_count == 0:
            print 'Number of reference_count is 0. Deleting cached object...'
            del self.__class__.cached_object

        print 'Deleted object. Count of objects = ', \
            self.__class__.reference_count


if __name__ == '__main__':
    proxy1 = Proxy()
    print ''

    proxy2 = Proxy()
    print ''

    proxy3 = Proxy()
    print ''

    proxy4 = Proxy()
    print ''

    proxy1.sort(reverse=True)
    print ''

    print 'Deleting proxy2'
    del proxy2
    print ''

    print 'The other objects are deleted upon program termination'