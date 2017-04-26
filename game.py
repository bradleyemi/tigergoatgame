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

class TigerGoatGame():
    def __init__(self):
        self.pieces = [piece(0, 'A1','t'),
                       piece(1, 'A5','t'),
                       piece(2, 'E1','t'),
                       piece(3, 'E5','t')]
        self.piece_id_counter = 4

        self.placed = 0
        self.goats_to_be_placed = 20
        self.eaten = 0
        self.turn = 'g'

        self.finished = False

    def show(self):
        draw_map(self.pieces, turn=self.turn, eaten=self.eaten, placed=self.placed)

    def is_move_valid(self, cmd):
        pass

    def move(self, cmd):
        pass

    def show_game_over(self):
        pass

def play():
    game = TigerGoatGame()
    while not game.finished:
        game.show()
        command = raw_input("\n-->")
        if game.is_move_valid(command):
            game.move(command)
        else:
            continue
    game.show_game_over()

menu()
        