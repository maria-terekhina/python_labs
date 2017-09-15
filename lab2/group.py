#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from operator import itemgetter
import re

__author__ = 'Мария Терехина'


class Person(object):
    """
    >>> sergey = Person('Sergey', 'Kabanov', 'man', date(1989, 4, 26))
    >>> print(sergey)
    Sergey, Kabanov, man, aged 28

    >>> sergey.full_ages()
    28
    >>> Person('Sergey', 'Kabanov', 'man', "1989.4.26")
    Traceback (most recent call last):
        ...
    ValueError: birthday must be date type.
    """

    def __init__(self, first_name, last_name, sex, birthday):

        res = re.search('....\-..\-..', str(birthday))
        if res is None:
            raise ValueError('birthday must be date type.')

        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.birtday = birthday
        self.age = Person.full_ages(birthday)

    def full_ages(self):

        if isinstance(self, Person):
            return self.age

        today = date.today()
        age = today.year - self.year

        if today.month < self.month:
            age -= 1
        elif today.month == self.month and today.day < self.day:
            age -= 1

        return age

    def __str__(self):

        sep = ', '

        return self.first_name + sep + self.last_name + sep + self.sex + sep +\
            'aged ' + str(self.age)


class Student(Person):

    def __init__(self, first_name, second_name, sex, birthday, course,
                    group, python_skill):

        res = re.search('....\-..\-..', str(birthday))
        if res is None:
            raise ValueError('birthday must be date type.')

        self.first_name = first_name
        self.last_name = second_name
        self.sex = sex
        self.birtday = birthday
        self.age = Person.full_ages(birthday)
        self.course = course
        self.group = group
        self.python_skill = python_skill


class Group(list):

    def sort_by_age(self, reverse=False):
        return self.sort(key=lambda x: x.age, reverse=reverse)

    def sort_by_name(self, reverse=False):
        return self.sort(key=lambda x: x.first_name, reverse=reverse)

    def sort_by_python_skill(self, reverse=False):
        return self.sort(key=lambda x: x.python_skill, reverse=reverse)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
