def boarders(a, b, num):

    '''
    This function cuts numbers according to boarders.
    >>> boarders(3,5,[1,4,5,7,8])
    '3 4 5 5 5'
    >>> boarders(-1.5,17,[-2.7,198,3.5])
    '-1.5 17 3.5'
    >>> boarders(6,7,[1,1,1])
    '6 6 6'
    '''

    for i in range(len(num)):
        if num[i] < a:
            num[i] = a
        elif num[i] > b:
            num[i] = b

    return ' '.join(list(map(str, num)))


def get_borders():

    try:
        board = list(map(float, input('Enter boarders\
separated by a space: ').split()))
    except:
        raise ValueError('Boarders must be \
numbers separated by a space')

    try:
        num = list(map(float, input('Enter numbers\
separated by a space: ').split()))
    except:
        raise ValueError('Arguments must be \
numbers separated by a space ')

    if not len(board) == 2:
        raise ValueError('There must be two boarder numbers')

    a, b = min(board), max(board)

    return boarders(a, b, num)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(get_borders())
