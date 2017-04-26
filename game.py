from __future__ import print_function
import os
from termcolor import colored
from environment import *

def menu():
    os.system('clear')
    while True:
        with open("introduction.txt") as f:
            for line in f.readlines():
                print(line,end='')
            print('')
        command1 = raw_input("---------->")
        if command1 == '':
            os.system('clear')
            play()
            os.system('clear')
            continue
        elif command1 == 'h':
            os.system('clear')
            with open("instructions.txt") as f:
                for line in f.readlines():
                    print(line,end='')
                print('')
            command2 = raw_input("--->")
            os.system('clear')
            continue
        elif command1 == 'q':
            break
        else:
            os.system('clear')
            continue
    os.system('clear')

def play():
    pieces = [piece(0, 'A1','t'),
              piece(1, 'A5','t'),
              piece(2, 'E1','t'),
              piece(3, 'E5','t')]
    draw_map(pieces)
    raw_input("\n-->")

menu()
        