def write_dict(d):
    '''
    This function prints  dictionary.
    >>> write_dict({'cat': ['dog']})
    cat - dog
    >>> write_dict({'cat': ['dog', 'mouse']})
    cat - dog, mouse
    >>> write_dict({'cat': ['dog'], 'mouse': ['dog'], 'wolf': ['mouse', 'cat']})
    cat - dog
    mouse - dog
    wolf - cat, mouse
    '''
    with open('output.txt', 'w') as f:
        for key in sorted(d.keys()):
            print(key + ' - ' + ', '.join(sorted(d[key])))
            f.write(key + ' - ' + ', '.join(sorted(d[key])) + '\n')


def create_latin(d):

    latin = {}

    for key in d:
        for word in d[key]:
            if word not in latin:
                latin[word] = [key]
            else:
                latin[word].append(key)

    return latin


def create_english():
    name = input('Input the file name with the extansion: ')

    with open(name, 'r') as f:
        lines = f.readlines()

    engl = {}

    for line in lines:
        time = line.split()
        engl[time[0]] = [i.strip(',') for i in time[2:]]

    return create_latin(engl)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    write_dict(create_english())
