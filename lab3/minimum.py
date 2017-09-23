#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def minimum(arg, *args, key=None):

    cmp = lambda lhs, rhs: lhs < rhs

    if not args:
        from collections import Iterable
        if not isinstance(arg, Iterable):
            raise ValueError('%s is not iterable object' % type(arg))

        result = next(iter(arg))
        for item in arg:
            if cmp(item, result):
                result = item
        return result

    else:
        result = arg1
        for item in args:
            if cmp(item, result):
                result = item
        return result


def main():
    pass


if __name__ == "__main__":
    main()
