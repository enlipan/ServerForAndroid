# -*-utf-8-*-

from abc import ABCMeta, abstractmethod


class A(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method(self, bar):
        pass

# class A(object):
#     # create class — type
#     __metaclass__ = object
#     pass


# print type(A)
# Child = type('Child', (object,), {'bar': 10})
# child = Child()
# print child.bar

print A


def echo(o):
    print o


echo(A)
A.new_attribute = 'new'
print hasattr(A, 'new_attribute')
print A.__class__


a = A()
