from __future__ import print_function
from collections import defaultdict
from termcolor import colored

# Map-relative row indices
ROW_INDEX = [1,6,11,16,21]
COL_INDEX = [4,12,20,28,36]

# Gameplay space names
ROW_NAMES = ['A','B','C','D','E']
COL_NAMES = ['1','2','3','4','5']

ROW_TO_INDEX = {}
COL_TO_INDEX = {}

for name, index in zip(ROW_NAMES, ROW_INDEX):
    ROW_TO_INDEX[name] = index

for name, index in zip(COL_NAMES, COL_INDEX):
    COL_TO_INDEX[name] = index

TURN = {'t': "#          It's TIGERS' turn.         #", \
'g':"#          It's GOATS' turn.          #"}
TURN_ROW = 6
STATS_ROW = 8

class piece:
    def __init__(self, id, space, owner):
        self.id = id
        self.space = space
        self.owner = owner
        self.row = ROW_TO_INDEX[space[0]]
        self.col = COL_TO_INDEX[space[1]]

    def move(self, space):
        self.space = space
        self.row = ROW_TO_INDEX[space[0]]
        self.col = COL_TO_INDEX[space[1]]

# Construct dictionary: keys are row-indices with any populated spaces,
# values are list of col-indices in the row that are populated
def populated_spaces_to_dict(pieces):
    populated_t_dict = defaultdict(list)
    populated_g_dict = defaultdict(list)
    for piece in pieces:
        if piece.owner == 't':
            populated_t_dict[piece.row].append(piece.col)
        elif piece.owner == 'g':
            populated_g_dict[piece.row].append(piece.col)
    return populated_t_dict, populated_g_dict

def draw_map(pieces, turn='g', eaten=0, placed=0):
    with open('title.txt') as f:
        for title_index, line in enumerate(f.readlines()):
            if title_index == TURN_ROW:
                print(TURN[turn])
            elif title_index == STATS_ROW:
                new_line = ""
                for character in line:
                    if character == 'Y':
                        new_line += str(placed)
                    elif character == 'Z':
                        new_line += str(eaten)
                    else:
                        new_line += character
                print(new_line,end='')
            else:
                print(line,end='')
    populated_t_dict, populated_g_dict = populated_spaces_to_dict(pieces)
    with open('map.txt') as f:
        for row_index, line in enumerate(f.readlines()):
            new_line = ""
            for col_index, character in enumerate(line):
                if col_index in populated_t_dict[row_index]:
                    new_line += colored('T', 'white', 'on_red')
                elif col_index in populated_g_dict[row_index]:
                    new_line += colored('G', 'white', 'on_blue')
                else:
                    new_line += character
            print(new_line, end='')
        print('')

def main():
    pieces_test = [piece(0, 'A1','t'),
                   piece(1, 'A5','t'),
                   piece(2, 'E1','t'),
                   piece(3, 'E5','t'),
                   piece(4, 'A3','g')]

    draw_map(pieces_test, turn='t', eaten=0, placed=1)

if __name__ == '__main__':
    main()
    