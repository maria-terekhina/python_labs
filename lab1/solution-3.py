from os import listdir, stat
from os.path import isfile, join


def printing(pairs):
    '''
    This function prints the files sorted by the size and the alphabet.
    >>> printing({611: ['3.py'], 7: ['q.txt', 'w.txt']})
    3.py
    q.txt
    w.txt
    '''

    for (size, names) in sorted(pairs.items(), reverse=True):
        for n in sorted(names):
            print(n)


def sort_of_files():
    mypath = input('Write a name of the directory: ')
    files = [(stat(f).st_size, f) for f in listdir(mypath)
if isfile(join(mypath, f))]

    pairs = {}

    for elem in files:
        if elem[0] in pairs:
            pairs[elem[0]].append(elem[1])
        else:
            pairs[elem[0]] = [elem[1]]

    printing(pairs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sort_of_files()
