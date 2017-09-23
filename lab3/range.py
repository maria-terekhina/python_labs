#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RangeIterator(object):
    '''
    Это итератор, принимающий на вход объект класса Range.

    >>> a = RangeIterator(Range(1, 6, 2))
    >>> next(a)
    1

    >>> next(a)
    3

    >>> next(a)
    5

    >>> next(a)
    Traceback (most recent call last):
    ...
    StopIteration
    '''

    def __init__(self, rg):
        self.rg = rg
        self.position = rg.start
        self.stop = rg.stop
        self.step = rg.step

    def __next__(self):

        i = self.position

        if self.position >= self.stop:
            raise StopIteration

        self.position += self.step

        return i


class Range(object):
    '''
    Это класс, задающий итерируемый объекты типа range.

     >>> a = Range(13, 153, 7)
    >>> print(a)
    Range(13, 153, 7)

    >>> if 20 in a: print('Yes')
    Yes

    >>> len(a)
    20

    >>> a[3]
    34

    >>> a[34]
    Traceback (most recent call last):
    ...
    IndexError: range object index out of range
    '''

    def __init__(self, *args):

        if len(args) not in range(1, 4):
            raise ValueError("This function must have frome 1 to 3 arguments")

        elif len(args) == 1:
            self.start, self.stop, self.step = 0, args[0], 1
        elif len(args) == 2:
            self.start, self.stop, self.step = args[0], args[1], 1
        elif len(args) == 3:
            self.start, self.stop, self.step = args[0], args[1], args[2]
        if self.step == 0:
            raise ValueError("step can't be 0")

    def __iter__(self):
        raise self

    def __repr__(self):
        return 'Range(%d, %d, %d)' % (self.start, self.stop, self.step)

    def __getitem__(self, key):
        if key >= len(self):
            raise IndexError('range object index out of range')

        i = 0
        k = self.start
        while i != key:
            k += self.step
            i += 1
        return k

    def __len__(self):
        return (self.stop-self.start+1)//self.step

    def __contains__(self, key):
        if key <= self.stop and key >= self.start \
                and (key - self.start) % self.step == 0:
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
