#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' The difference between __init__ and __new__.

1) __new__ creates and returns the instance of the class or returns None.
   __init__ does not create anything, it is just inizialize the instance
   created by __new__ and returns nothing.
2) __init__ takes as arguments all argument with which class was called.
    __new__ takes the class as s first argument and also takes all __init__
    arguments to create them.
'''


class feature_one_1(float):

    '''Convert from centimeter to meter. This will work.
    >>> print(feature_one_1(100.0))
    1.0
    '''

    def __new__(cls, arg=1.0):
        return float.__new__(cls, arg*0.01)


class feature_one_2(float):

    '''Convert from centimeter to meter.
    This will not work, because the float type's __init__ if not an operation.
    It returns ignoring the arguments.
    '''

    def __init__(self, arg=0.0):
        return float.__new__(self, arg*0.01)


class feature_two(object):

    '''Show the order of methods.
    This class prints some messages to show that the __init__ method
    calls after the __new__.
    >>> feature_two(); feature_two()
    NEW
    INIT
    ...
    It already exists
    INIT
    ...
    '''

    new_dict = dict()

    def __new__(cls):

        if 'key' in feature_two.new_dict:
            print('It already exists')
        else:
            print('NEW')

        return object.__new__(cls)

    def __init__(self):
        print ('INIT')
        feature_two.new_dict['key'] = self


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
