"""Raymond Hettinger's Super Lesson.

"""
import collections
import logging
log = logging.getLogger(__name__)
log.propagate = False
log.setLevel(logging.INFO)

# Remove old handlers to allow updating settings
for handler in list(log.handlers):
    log.removeHandler(handler)
# create console handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)

# add the formatter to the handler
formatter = logging.Formatter('%(name)s - %(asctime)-15s - %(levelname)s: %(message)s')
stream_handler.setFormatter(formatter)

# setup logger and add the handlers
log.addHandler(stream_handler)


class LoggingDict(dict):
    """Extending a Built-in.

    We are going to extend the `dict` built-in by adding a logging call to
    the dictionary, by over-riding adding a key-value pair.
    """
    def __setitem__(self, key, value):
        """Add a logging call.

        The built-in `dict` already has a __setitem__ method that allows new
        key-value pairs to be inserted after creation. We merely add a
        logging message to this sub-class of the built-in, and use `super` to
        call the base `dict` set item. It is an in-direct reference call,
        meaning that if we were to swap the `dict` base with another object
        then `super` would immediately extend to the new object.
        """
        log.info("Setting {}:{} pair.".format(key, value))
        super().__setitem__(key, value)


class LoggingOrderedDict(LoggingDict, collections.OrderedDict):
    """Extending via Method Resolution Order.

    Not only is `super()` an in-direct reference, but it is computed at run
    time. That means that we can modify order at which methods are resolved
    by ordering the mix-in bases. The ancestry of this class is:

    `LoggingDict`, `OrderedDict`, `dict`, `object`

    When calling LOD, the MRO passes to LoggingDict, which adds the logging
    call. However, it then passess to `OrderedDict` because LD is resolved
    before OD. Note, however, that as of python 3.7 `dict`s preserve key
    entry order. OD's still preserve ordering in equality:

    OD(a=1, b=2) != OD(b=2, a=1) .BUT. D(a=1, b=2) == D(b=2, a=1)
    """
    pass


if __name__ == "__main__":
    print("Initiating LoggingDict(a=1, hello='world')")
    X = LoggingDict(a=1, hello='world')
    print("Adding new key value pair b, 1.0")
    X['b'] = 1.0

    print("Repeat, but for LoggingOrderedDict.")
    X = LoggingOrderedDict(a=1, hello='world')
    X['b'] = 1.0

