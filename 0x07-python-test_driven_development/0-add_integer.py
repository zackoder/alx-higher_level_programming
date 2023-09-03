#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    
    """
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        """ Check if a is an integer or a float and cast it to an integer if needed """
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        """ Check if b is an integer or a float and cast it to an integer if needed """
        raise TypeError("b must be an integer")
    """ Return the addition of a and b """
    return (int(a) + int(b))
