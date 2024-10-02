"""Python Riddles!"""
import copy
import itertools

URL = "/".join(("https:/", "medium.com", "@moraneus",
                "think-you-know-python-these-20-riddles-will-make-you-think-again-f4b811ca0e5f"))

def one():
    """List Mutability.

    This tests how python assigns objects to namespaces. Python does not
    assign objects to new memory addresses if giving it a new namespace. In
    this example, `y = x` sets `y` as a *pointer* to x as opposed to a copy
    of `x`. This is why you have to be careful when you use the assign OP,
    and why the copy module exists.
    """
    x = [1, 2, 3]
    y = x
    y.append(4)
    assert x == [1, 2, 3, 4]


def two():
    """Default mutable arguments.

    I got this wrong. A mutable default argument can cause trouble because
    the function here acts as a static method within the main function.
    Since a list is mutable, and func() is bound to a namespace within two,
    subsequent calls within two will append to the same object b. However,
    if two received an argument that was a list of values, then each series
    of calls to func resets b.
    """
    def func(a, b=[]):
        b.append(a)
        return b
    assert func(1) == [1]
    assert func(2) == [1, 2] # != [2]
    assert func(3) == [1, 2, 3] # != [3]


def twoAlt(x):
    """"Default mutable arguments.

    Because x is passed into twoAlt, func has to be accessed each time a new
    series is passed to func.
    """
    def func(a, b=[]):
        b.append(a)
        return b
    for i, y in enumerate(x):
        assert func(y) == x[:i+1]


def three():
    """Multiple assignment.

    Swapping variables here works along the same argument as riddle one.
    The swap line swaps pointer addresses to memory as opposed to actual
    values.
    """
    a, b = 1, 2
    a, b = b, a
    assert a == 2
    assert b == 1


def four():
    """Boolean arithmetic.

    Python autocasts between `bool` and other values in a seamless way.
    However, this abstraction can cause trouble.
    """
    assert True + True + True == 3


def five():
    """String indexing and slicing.

    Python does treat strings as an array of characters, which is inherited
    from C.
    """
    assert "hello"[-1] + "world"[1] == "oo"


def six():
    """String formatting with f-strings.

    Python adding f-strings, the ability to on-the-fly format objects for
    string representations without using the format keyword, makes printing
    (logging) much more robust. One does not replace the other, but you can
    choose the way that works for you. One good thing about f-strings is you
    can evaluate expressions on the fly.
    """
    x, y = 10, 50
    assert f"{x}% of {y} is {x/100*y}" == "10% of 50 is 5.0"


def seven():
    """Operator precedence.

    Python abides by mathematical operator precedence. However, this can
    burn you if, for example, you wanted the second or third expression.
    Using brackets can help you by being explicit.
    """
    assert 2 * 3 ** 3 * 2 == 2**2 * 3**3 == 108
    assert 2 * 3 ** (3 * 2) == 2 * 3 ** 6 == 2 * 729 == 1458
    assert (2 * 3) ** (3 * 2) == 6 ** 6 == 2 ** 6 * 3 ** 6 == 46656


def eight():
    """Function returns and string concatenation.

    This is a weird one. Why is this a riddle?
    """
    def greet(name):
        return f"Hello, {name}!"
    assert greet("Alice") + " " + greet("Bob") == "Hello, Alice! Hello, Bob!"


def nine():
    """Using the `range` function.
    
    Remember that the range function generates a domain where only the left
    (start) value is included, and the right (stop) value is excluded.
    """
    assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]


def ten():
    """String formatting with format method.

    Calling back to riddle six, we see another reason for why the format
    method cannot be replaced by f-strings. Since str.format is a class
    method, it supports indexing of arbitrary arguments.
    """
    assert "{2}, {1}, {0}".format("a", "b", "c") == "c, b, a"


def eleven():
    """Set operations. Amazing."""
    assert len(set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])) == 4


def twelve():
    """Dictionary copying.

    In riddles one and two we talked about copying and namespaces, and the
    use of the `copy` module in python. Although the riddle only asks about
    the second assert, we will go over how shallow and deep copies work.

    The first assert replicates what we already demonstrated in riddle one:
    that assigning an object to another object acts as a pointer to the
    same memory address.
    
    In the second test, passing a dictionary through the `dict` typedef by
    default utilizes a shallow copy.

    Since shallow copy does not traverse deeper than the first level of an
    object, deeper layers still point to the same space in memory. This is
    due to how python addresses memory depending on object type.
    """
    x = {"a": 1, "b": 2}
    y = x
    y["c"] = 3
    assert x == y == {"a": 1, "b": 2, "c": 3}
    
    x = {"a": 1, "b": 2}
    y = dict(x)
    y["c"] = 3
    assert x == {"a": 1, "b": 2}
    assert y == {"a": 1, "b": 2, "c": 3}

    x = {"a": 1, "b": 2, "c": [1, 2]}
    y = dict(x)
    y["c"].append(3)
    y["d"] = 4
    assert x == {"a": 1, "b": 2, "c": [1, 2, 3]}
    assert y == {"a": 1, "b": 2, "c": [1, 2, 3], "d": 4}
    
    x = {"a": 1, "b": 2, "c": [1, 2]}
    y = copy.deepcopy(x)
    y["c"].append(3)
    y["d"] = 4
    assert x == {"a": 1, "b": 2, "c": [1, 2]}
    assert y == {"a": 1, "b": 2, "c": [1, 2, 3], "d": 4}


def thirteen():
    """List comprehensions and character manipulation."""
    assert "".join([chr(ord(c) + 1) for c in "hello"]) == "ifmmp"


def fourteen():
    """Type coercion in multiplication.

    I originally had this wrong because I thought somewhere in there python
    had decided to try to cast string to floats. However, as soon as it
    failed I knew the right answer. Certain types, like strings and lists,
    use the multiplication OP to act like a repeater.
    """
    def multiply(a, b):
        return a * b
    assert multiply(3, "5") == 3 * "5" == "555" # != 15


def fifteen():
    """Functional programming - map and sum."""
    assert sum(map(int, "123")) == 6


def sixteen():
    """Boolean conversions.

    Remember that everything but 0 and None is cast to True. Usecases for
    this include codepath trees based on whether functions are executed.
    """
    assert bool("False") is True
    assert bool(-1) is True
    assert bool(None) is False
    assert bool(0) is False


def seventeen():
    """List slicing. Original riddle is the first test."""
    x = [1, 2, 3]
    assert x[::-1] == [3, 2, 1]
    assert x == [1, 2, 3]
    x.reverse()
    assert x[::-1] == [1, 2, 3]
    assert x == [3, 2, 1]
    
    


def eighteen():
    """Rounding behaviour.

    Python builtin `round` uses numerical and not mathematical rounding.
    Mathematical rounding uses the definition:
    ROUND(x):=CEIL(x) IF MOD(x,1)>=0.5 ELSE FLOOR(x)
    Numerical rounding modifies this definition when MOD(x,0.5)=0, that is,
    when the value is an integer + 1/2. In this situation, to enforce
    numerical stability as roundoff errors collect in a long calculation,
    an odd integer is rounded up but an even intenger is rounded down.
    """
    assert round(5.5) == 6
    assert round(6.5) == 6


def nineteen():
    """Testing the itertools module.

    This I only figured out after reading the docstring. Note that the
    `permutations` function is a generator of *tuples*, so you need to wrap
    it in a container like a list. I made the mistake of assuming it
    returned a `list` of `list`s instead of a `list` of `tuple`s.
    """
    assert list(itertools.permutations([1, 2, 3], 2)) == [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]


def twenty():
    """The eval function. Note we can use globals and locals here."""
    assert eval("2 + 3 * 4") == eval("2 + a * b", {"a": 3, "b": 4}) == 14


if __name__ == "__main__":
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()
    ten()
    eleven()
    twelve()
    thirteen()
    fourteen()
    fifteen()
    sixteen()
    seventeen()
    eighteen()
    nineteen()
    twenty()
