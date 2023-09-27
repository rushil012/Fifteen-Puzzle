# author: Rushil Nagpal
# date: May 26, 2023
# file: fifteen.py , a class which has the functions for fifteen puzzle game
# input: the move number
# output: the result of the move
import numpy as np
from random import choice
class Fifteen:
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.size = size
        self.adj =  {
        0: [1, 4],
        1: [0, 2, 5],
        2: [1, 3, 6],
        3: [2, 7],
        4: [0, 5, 8],
        5: [1, 4, 6, 9],
        6: [2, 5, 7, 10],
        7: [3, 6, 11],
        8: [4, 9, 12],
        9: [5, 8, 10, 13],
        10: [6, 9, 11, 14],
        11: [7, 10, 15],
        12: [8, 13],
        13: [9, 12, 14],
        14: [10, 13, 15],
        15: [11, 14]
    }
    def update(self, move):
        if self.is_valid_move(move):
            move_index = np.where(self.tiles == move)[0][0]
            empty_index = np.where(self.tiles == 0)[0][0]
            self.transpose(move_index,empty_index)
        # Swap the empty space with the move tile
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index],self.tiles[move_index] =self.tiles[move_index],self.tiles[index]
            index = move_index
    def is_valid_move(self, move):   #9
        move_index = np.where(self.tiles == move)[0][0]
        for i in self.adj[move_index]:
            if self.tiles[i] == 0:
                return True 
        return False #4
        # Check if the move index is adjacent to the empty index
         # Down
    def is_solved(self):
        for i in range(1, (self.size * self.size) - 1):
            if self.tiles[i-1] != i:
                return False
        return self.tiles[-1] == 0
    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print('+---+---+---+---+')
        for row in range(self.size):
            print('|', end='')
            for col in range(self.size):
                tile = self.tiles[row * self.size + col]
                if tile == 0:
                    print('   ', end='|')
                else:
                    print(f'{tile:2} ', end='|')
            print('\n+---+---+---+---+')
    def __str__(self):
        tiles_str = [str(tile) if tile != 0 else "" for tile in self.tiles]
        return f' {tiles_str[0]} {tiles_str[1]} {tiles_str[2]} {tiles_str[3]} \n {tiles_str[4]} {tiles_str[5]} {tiles_str[6]} {tiles_str[7]} \n {tiles_str[8]} {tiles_str[9]} {tiles_str[10]} {tiles_str[11]} \n{tiles_str[12]} {tiles_str[13]} {tiles_str[14]}{tiles_str[15]} \n'

if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n'
    game.update(15)
    assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n'
    assert game.is_solved() == False
    '''You should be able to play the game if you uncomment the code below'''




    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')


