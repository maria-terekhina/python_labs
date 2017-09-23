#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from chain import chain


def test_simple():

    assert [1] == [i for i in chain(1)]
    assert [1, 2, 3] == [i for i in chain(1, 2, 3)]
    assert [1, 2, 3, 4] == [i for i in chain([1, 2], [3, 4])]


def test_middle():

    assert [1, 2, "t", "e", "s", "t"] == [i for i in chain([1, 2], ["test"])]
    assert [1, 2, 3, 4, 5] == [i for i in chain([1, 2, {3: "a", 4: "b"}], [[[{5: "c"}]]])]
    assert ["t", "e", "s", "t"] == [i for i in chain([[[[[["test"]]]]]])]


def test_hard():

    assert list(range(1, 99)) == [i for i in chain(list(zip(range(1, 100, 2),
                                                            [([[i]]) for i in range(2, 100, 2)])))]
