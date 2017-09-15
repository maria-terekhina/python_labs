def polindrom(s=input('Write yort text: ')):

    '''
    This funcrion checks if the text is polindrom.
    >>> polindrom('mama')
    not a polindrom
    >>> polindrom('aAaaaaa')
    polindrom
    >>> polindrom('Go to hell')
    not a polindrom
    '''

    strk = [i for i in s.lower()]
    reverse = strk[::-1]

    if strk == reverse:
        print('polindrom')
    else:
        print('not a polindrom')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    polindrom()
