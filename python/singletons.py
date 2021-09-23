"""Pythonic implementations of Singletons.

Singles are a design choice in python. When initiated, they point to the
same space in memory. This means there is only one object of its kind in
existance, and every other assignment is just a pointer to this one
space in memory. It is essentially a very restrictive instance of a
global variable. Taken from a post on stackoverflow by ...
"""
__author__ = "https://stackoverflow.com/users/655372/theheadofabroom"

def singleton(cls):
    """Generate singletons using a decorator.

    The first method is to build a singleton decorator. The beauty of this
    method is you can decorate multiple types of singletons for your use. As
    we shall see, there are other methods of generating a singleton object,
    and so multiple singletons in those cases will require multiple class
    inheritances. There are several reasons why you might not want to use a
    decorator, though. The objects created using decorated class are
    singletons, the decorated class is not a class itself, but rather a
    function. Thus, you cannot call class methods from it.

    TheHeadOfaBroom offers a way to build a decorator returns a class with
    the same name. The decorating class becomes a class itself, and so you
    can use class inheritance automatically as with method 3 below. However,
    it may not scale because you have to create two classes for each new
    singleton class you decorate. You also cannot `super()` base classes as
    in method 3 because you will get a recursion error, preventing you from
    customizing methods like __new__ and calling up to __init__ from a
    subclass.
    """
    instances = {}

    def getinstance(*args, **kwargs):
        """Get the instance of the singleton object."""
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance


class Singleton(object):
    """Generate singletons using a base class.

    The second method is to use a true class to build a singleton. This has
    the opposite pros and cons as the decorator. As a true class, you can
    call methods from it. However, multiple types of singletons require
    multiple inheritances from this base class. Another problem is that
    methods like __new__ could be accidentally overwritten by other base
    classes.
    """
    _instance = None
    
    def __new__(self, *args, **kwargs):
        if not isinstance(self._instance, self):
            self._instance = object.__new__(self, *args, **kwargs)
        return self._instance


class MetaSingleton(type):
    """Generate singletons using a metaclass.

    The third method is to use the __metaclass__ attribute to define how the
    MetaSingleton class will behave. We now have a true singleton class that
    will prevent methods being overwritten by inheritance from siblings. I
    am positive this is what the metaclass was designed to do. Note that
    it is actually impossible to generate a metaclass in pure python, so we
    need to use `type` as the base because it is iteself a metaclass. Weird.
    """
    _instances = {}
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(MetaSingleton, self).__call__(*args, **kwargs)
        return self._instances[self]


def printing(x, y, t):
    print("x is ", x)
    print("y is ", y)
    print("t is ", t)
    print("does x == y?", x == y)
    print("does t != x, y?", x != t, y != t)
    print(20 * "- -")


if __name__ == "__main__":
    print("""Using a comparison:

    class Comparison(object):
        pass

    x = Comparison()
    y = Comparison()
    t = type(x)()""")

    class Comparison(object):
        pass
    x = Comparison(); y = Comparison(); t = type(x)(); printing(x, y, t);

    print("""Using the decorator method:

    @singleton
    class ObjectBeingDecorated(object):
        pass

    x = ObjectBeingDecorated()
    y = ObjectBeingDecorated()
    t = type(x)()""")
    @singleton
    class ObjectBeingDecorated(object):
        pass
    x = ObjectBeingDecorated(); y = ObjectBeingDecorated(); t = type(x)(); printing(x, y, t);

    print("""Using the class method:

    class ObjectBeingClassed(Singleton, object):
        pass

    x = ObjectBeingClassed()
    y = ObjectBeingClassed()
    t = type(x)()""")
    class ObjectBeingClassed(Singleton, object):
        pass
    x = ObjectBeingClassed(); y = ObjectBeingClassed(); t = type(x)(); printing(x, y, t);
    
    print("""Using the metaclass method:

    class ObjectBeingMeta(object, metaclass=MetaSingleton):
        pass

    x = ObjectBeingMeta()
    y = ObjectBeingMeta()
    t = type(x)()""")
    class ObjectBeingMeta(object, metaclass=MetaSingleton):
        pass
    x = ObjectBeingMeta(); y = ObjectBeingMeta(); t = type(x)(); printing(x, y, t)
