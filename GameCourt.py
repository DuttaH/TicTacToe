import os


def spline(size, char1, char2):
    if size % 2 == 1:
        size += 1
    tlen = size * 3
    for i in range(1, tlen):
        if i % size == 0:
            print(char1, end='')
        else:
            print(char2, end='')
    print()


def printmove(size, row):
    if size % 2 == 1:
        size += 1
    tlen = size * 3
    index = 0
    printindex = size / 2
    for i in range(1, tlen):
        if i % size == 0:
            print('|', end='')
        elif i == printindex:
            print(row[index], end='')
            index += 1
            printindex = printindex + size
            if index == 3:
                break
        else:
            print(' ', end='')
    print()


def print_court(ct, size):
    os.system('clear')
    ct_list = list(ct.values())
    spline(size, '|', ' ')
    printmove(size, ct_list[0:3])
    spline(size, '|', ' ')
    spline(size, '+', '-')
    spline(size, '|', ' ')
    printmove(size, ct_list[3:6])
    spline(size, '|', ' ')
    spline(size, '+', '-')
    spline(size, '|', ' ')
    printmove(size, ct_list[6:9])
    spline(size, '|', ' ')
