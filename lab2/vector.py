#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt


class Vector:
    '''
    Class Vector is n-dimensional array.

    Examples of usage:

    >>> vec1 = Vector([1, 2, 3, 4])
    >>> vec2 = Vector([0, 1, -1, -4])

    >>> vec1
    Vector([1, 2, 3, 4])

    >>> vec1 + vec2
    Vector([1, 3, 2, 0])

    >>> vec1 - vec2
    Vector([1, 1, 4, 8])

    >>> print(vec1 * vec2)
    Vector([0, 2, -3, -16])
    
    >>> print(vec2 / vec1)
    Vector([0.0, 0.5, -0.3333333333333333, -1.0])
    
    >>> vec1 == Vector([1, 2, 3, 4])
    True

    >>> vec1.append(144)
    >>> print(vec1)
    Vector([1, 2, 3, 4, 144])

    >>> len(vec1)
    5

    >>> vec1[1] == 2
    True

    >>> vec1[-1] = 5
    >>> vec1[-1]
    5
    
    >>> vec1.clear()
    >>> if not vec1: print('Vector is empty!')
    Vector is empty!

    >>> vec2.reverse()
    >>> vec2
    Vector([-4, -1, 1, 0])

    >>> abs(vec2) == sqrt(16 + 1 + 1 + 0)
    True
    
    >>> vec2.argmin()
    0
    >>> vec2[vec2.argmin()] == -4
    True
    >>> vec2.argmax()
    2
    >>> vec2[vec2.argmax()] == 1
    True

    '''

    def __init__(self, arr):
        self.arr = arr
       
        
    def __add__(self, other):
        return Vector([self.arr[i] + other.arr[i] for i in range(len(self.arr))])

        
    def __sub__(self, other):
        return Vector([self.arr[i] - other.arr[i] for i in range(len(self.arr))])
    

    def __mul__(self, other):
        return Vector([self.arr[i] * other.arr[i] for i in range(len(self.arr))])

    
    def __truediv__(self, other):
        return Vector([self.arr[i] / other.arr[i] for i in range(len(self.arr))])
    
   
    def __repr__(self):
        return 'Vector(%s)' % (str(self.arr))
    
    
    def __eq__(self, other):
        if self.arr == other.arr:
            return True
        else:
            return False

        
    def __abs__(self):
        return sqrt(sum([i**2 for i in self.arr]))
    

    def __setitem__(self, key, val):
        if key == -1 or key == len(self):
            return self.arr.append(val)
        else:
            raise ValueError('This index already exists')
        
    
    def __getitem__(self, key):
        return self.arr[key]
    

    def __len__(self):
        return len(self.arr)
    

    def append(self, el):
        Vector(self.arr.append(el))
        

    def reverse(self):
        self.arr.reverse()
        

    def argmax(self):
        return self.arr.index(max(self.arr))
    

    def argmin(self):
        return self.arr.index(min(self.arr))
    

    def clear(self):
        return self.arr.clear()
        
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
