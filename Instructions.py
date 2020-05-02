# This this package to print game instructions
import pandas as pd
import os

menu = ['  1. New Game',
        '  2. New Game - Multi player',
        '  3. Continue previous game',
        '  4. Settings',
        '  5. Help',
        '  0. Exit',
        ]


def hline(len):
    for i in range(len + 2):
        if i == 0 or i == len + 1:
            print('+', end='')
        else:
            print('-', end='')
    print()


def fittext(text, width, sp_ch):
    ftext = ''
    lpad = 7
    rpad = 6
    fline = True
    newline = sp_ch + '\n'
    ch = 0
    while len(text) > width:
        ch = text[:width].rfind(' ')
        if fline:
            ftext = text[:ch].ljust(width + rpad) + newline
            fline = False
        else:
            ftext += sp_ch + text[:ch].rjust(len(text[:ch]) + lpad).ljust(width + lpad + rpad) + newline
        text = text[ch:].lstrip()
    if fline:
        ftext = text.ljust(width + rpad) + sp_ch
    else:
        ftext += sp_ch + text[:ch].rjust(len(text[:ch]) + lpad).ljust(width + lpad + rpad) + sp_ch
    return ftext


def print_help(hold):
    os.system('cls')
    df = pd.read_excel(r'RulesDB.xlsx')
    rules = df[:].values
    hline(63)
    print('Instructions'.center(63))
    hline(63)
    for rule in rules:
        print('|', str(rule[0]).rjust(3), '.', fittext(rule[1], 50, '|'))
    hline(63)
    if hold:
        input('Press any key to continue...')
        return


def print_menu(cls):
    if cls:
        os.system('cls')
    hline(63)
    print('Menu'.center(63))
    hline(63)
    for items in menu:
        print('|', fittext(items, 56, '|'))
    hline(63)
