import sys
import random


class game_board:

    def __init__(self):
        self.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, '10']

    def print_board(self):
        print(f'{self.data[6]}|{self.data[7]}|{self.data[8]}')
        print(f'{self.data[3]}|{self.data[4]}|{self.data[5]}')
        print(f'{self.data[0]}|{self.data[1]}|{self.data[2]}')
    
    def insert_data(self, val, pos):
        self.data[pos-1] = val

    def check_valid(self, pos):
        return type(self.data[pos-1]) == type(2)
    
    def check_draw(self):
        for val in self.data:
            if type(val) == type(2):
                return False
        return True

    def check_win(self):
        return (self.data[0] == self.data[1] == self.data[2] or 
                self.data[3] == self.data[4] == self.data[5] or
                self.data[6] == self.data[7] == self.data[8] or
                self.data[6] == self.data[3] == self.data[0] or
                self.data[7] == self.data[4] == self.data[1] or 
                self.data[8] == self.data[5] == self.data[2] or
                self.data[0] == self.data[4] == self.data[8] or
                self.data[6] == self.data[4] == self.data[2])
    

class Spacing:

    @staticmethod
    def fresh_screen():
        for _ in range(20):
            print('')

    @staticmethod
    def one_space():
        print('')
    
    @staticmethod
    def two_space():
        print('')
        print('')


def anton(board):
    posible = []
    for val in board:
        if type(val) == type(2):
            posible.append(val)
    return random.choice(posible)

             
if __name__ == '__main__':
 
    cur_board = game_board()
 
    # intro
    Spacing.fresh_screen()
    print('Welcome to Tic Tac Toe (Made in an hour)')
    Spacing.one_space()
    player_name = input('Please enter your name: ')
    Spacing.two_space()
    print(f'Hello {player_name}, my name is Anton. Lets play some tic tac toe')
    print('Game Rules:')
    Spacing.one_space()
    print('1. If at any point you need to quit the game press ctrl c')
    print('2. To pick a position press the associated number')
    print('3. Get three xs in a row to win')
    Spacing.fresh_screen()
    cur_board.print_board()
    Spacing.one_space()

    while True:

        # player's move
        player_pos = 10
        while not cur_board.check_valid(player_pos):
            try:
                print(f'{player_name}, press the number where you want to place your piece')
                player_pos = int(input('Your choice: '))
                if player_pos < 1 or player_pos > 9:
                    player_pos = 10
                    raise
            except:
                Spacing.one_space()
                print('Have to input a valid number')
                Spacing.one_space()
        cur_board.insert_data(val='x', pos=player_pos)

        Spacing.fresh_screen()
        cur_board.print_board()
        Spacing.one_space()

        if cur_board.check_win():
            print(f'{player_name}! You just won')
            sys.exit() 
        
        if cur_board.check_draw():
            print('You were a worthy opponet, its a draw')
            sys.exit()

        # anton's move
        print(f'Nice move {player_name}, but you better watch out...')
        Spacing.one_space()
        cur_board.insert_data(val='o', pos=anton(cur_board.data[:9]))

        cur_board.print_board()
        Spacing.one_space()

        if cur_board.check_win():
            print('I Anton have won! Better luck next time')
            sys.exit() 
        