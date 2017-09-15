def factorial(n):
    '''
        Function calculate factorial of integer using recursion.
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> [factorial(i) for i in range(5)]
    [1, 1, 2, 6, 24]
    >>> factorial('121')
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer

    >>> factorial([1])
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer

    >>> factorial(1.12)
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be integer

    >>> factorial(-10)
    Traceback (most recent call last):
        ...
    ValueError: Argument n must be nonnegative

    >>> import math
    >>> n = 1000
    >>> math.factorial(n) == factorial(n)
    True
    '''

    if not isinstance(n, int):
        raise ValueError('Argument n must be integer')

    if not n >= 0:
        raise ValueError('Argument n must be nonnegative')

    answer = 1

    for i in range(1, n+1):
        answer = answer * i

    return answer


def test_factorial():
    assert factorial(5) == 120
    import math
    assert factorial(1000) == math.facorial(1000)


def test_type_error(self):
    with pytest.raises(TypeError):
        factorial([1])
    with pytest.raises(TypeError):
        factorial('12')

if __name__ == '__main__':
    import doctest
    import pytest
    doctest.testmod()
