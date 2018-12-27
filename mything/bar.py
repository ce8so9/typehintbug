from mything.foo import Foo

def my_function(myparam: Foo) -> Foo:
    """Takes a foo and returns it.

    :param myparam: Can't click the type.

    :returns: See the the type annotation. You should be able to click it.
    """
    return myparam

def other_function(myparam):
    """Manual type and rtype here.

    :param myparam: Click the type it works
    :type myparam: Foo

    :returns: The foo you gave it
    :rtype: Foo
    """
    return myparam
