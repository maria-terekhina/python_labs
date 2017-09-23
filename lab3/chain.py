#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable


def chain(*args):

    if not args:
        raise ValueError('Function called without arguments!')

    for elem in args:
        if isinstance(elem, Iterable):
            if isinstance(elem, str):
                for letter in elem:
                    yield letter
            else:
                yield from list(chain(elem))
        else:
            yield elem


def main():
    pass


if __name__ == "__main__":
    main()
