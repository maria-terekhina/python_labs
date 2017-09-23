#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import filterfalse


def unique(iterable):
    """
    Unique generator. Generate unique values of iterable object.

    :param iterable: iterable object

    Example of usage:
    >>> for i in unique([1, 2, 1, 3, 1, 4, 4, 5, 6]): print(i)
    1
    2
    3
    4
    5
    6
    """

    from collections import Iterable

    if not isinstance(iterable, Iterable):
        raise ValueError('%s is not iterable object' % type(iterable))

    result = set()
    for elem in filterfalse(result.__contains__, iterable):
            result.add(elem)
            yield elem

if __name__ == "__main__":
    import doctest
    doctest.testmod()
