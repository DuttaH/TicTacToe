from Instructions import *
from GamePlay import *
import os

choice = ''
print_help(False)
print_menu(False)
while choice != '0':
    choice = input('Enter your choice: ')
    if choice == '1':
        new_game()
    if choice == '5':
        print_help(True)
    if choice == '0':
        os.system('clear')
        break
    print_menu(True)
