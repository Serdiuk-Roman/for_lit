"""
    argparse



import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

"""


class Bar:
    A = "trololo"

    @property
    def foo(self):
        return self.x

    @foo.setter
    def foo(self, value):
        self.x = value ** 2

    @foo.deleter
    def foo(self):
        del self.x


# bar = Bar()
# print(bar.__dict__)
# bar.foo = 5
# print(bar.__dict__)
# print(bar.foo)

# class Bar3:
#     def __get__(self, obj, cls=None):
#         pass

#     def __set__(self, obj, value):
#         pass

#     def __delete__(self, obj):
#         pass

# garbage collector почитати
# дескриптор данных(get, set)

class Property:
    def __init__(self, getter, setter, deletter):
        self.g = getter
        self.s = setter
        self.d = deletter

    def __get__(self, obj, cls=None):
        if self.g is None:
            raise AttributeError
        return self.g(obj)

    def __set__(self, obj, value):
        if self.s is None:
            raise AttributeError
        self.s(obj, value)

    def __delete__(self, obj):
        if self.d is None:
            raise AttributeError
        self.d(obj)


class Bar2:
    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x ** 2

    def del_x(self):
        del self._x

    foo = Property(get_x, set_x, del_x)


# bar2 = Bar2()
# bar2.foo = 2
# print(bar2.foo)

# почитати staticmethod i classmethod i baundmethod
# class Staticmethod:
#     def __init__(self, f):
#         self.f = f

#     def __get__(self, obj, cls=None):
#         # ?????
#         pass

# obj < Class < MetaClass

class Square(int):
    def __new__(cls, n):
        return super().__new__(cls, n ** 2)
# print(Square(5))


from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])

# p = Person(name="vasia", age=25)
# print(p.name)
# print(p.age)

class Person(Person):
    def __new__(cls, *a, **kw):
        kw["name"] = kw["name"].title()
        return super().__new__(cls, *a, **kw)

p = Person(name="vasia", age=25)
print(p.name)
