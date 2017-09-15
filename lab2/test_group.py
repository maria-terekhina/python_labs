import pytest

from math import inf
from group import date
from group import Group, Student


def make_test_group():
    sergey = Student("Сергей", "Кабанов", "man",
                     date(1989, 4, 26), None, None, 1)
    masha = Student("Маша", "Абстрактная", "woman",
                    date(1998, 3, 8), 3, 151, -inf)
    dictator = Student("Гвидо", "ван Россум", "man",
                       date(1900, 1, 1), None, None, inf)

    return Group([dictator, sergey, masha])


def test_group_sorting_methods():

    group = make_test_group()

    sorted_ages = []
    group.sort_by_age()
    for student in group:
        sorted_ages.append(student.full_ages())

    assert [19, 28, 117] == sorted_ages

    sorted_skills = []
    group.sort_by_python_skill(reverse=True)
    for student in group:
        sorted_skills.append(student.python_skill)

    assert [inf, 1, -inf] == sorted_skills

    sorted_names = []
    group.sort_by_name()
    for student in group:
        sorted_names.append(student.first_name)

    assert ['Гвидо', 'Маша', 'Сергей'] == sorted_names

make_test_group()
test_group_sorting_methods()
