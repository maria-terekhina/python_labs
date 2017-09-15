#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
При ромбовидном наследовании происходит следующее: существует класс А,
от которого наслудуют классы B и C и класс Dб который наследует от B и C.
Может слуаться так, что в классах В и C один и тот же метод определн
по-разному. При этом возникает неоднозначность, какую именно реализацию
метода должен в таком случае унаследовать класс D?
В питоне проблема решается слудующим образом: наследуем у класса, который был
создан позже.
'''


class Vector_A:

    def __init__(self, arr=[]):
        self.arr = arr


class Vector_C(Vector_A):

    '''
    Длина в Vector_C определяется как длина массива, хранящегося в self.arr.
    '''

    def __init__(self, arr=[]):
        self.arr = arr

    def __len__(self):
        return len(self.arr)


class Vector_B(Vector_A):

    '''
    Длина в Vector_B определяется как длина строковой записи массива,
    хранящегося в self.arr. Странно, но возможно.
    '''

    def __init__(self, arr=[]):
        self.arr = arr

    def __len__(self):
        return len(str(self.arr))


class Vector_D(Vector_B, Vector_C):

    '''
    Метод len() будет унаследован у класса Vecror_B

    >>> vec = Vector_D([1, 2, 3, 4])
    >>> len(vec)
    12
    '''
    def __init__(self, arr):
        self.arr = arr


if __name__ == '__main__':
    import doctest
    doctest.testmod()
