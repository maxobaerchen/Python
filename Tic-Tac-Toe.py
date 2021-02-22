#!/bin/python

class TicTacToe:

    def __init__(self):
        self.first_row = ['_', '_', '_']  # Initializing a TicTacToe bord
        self.second_row = ['_', '_', '_']
        self.third_row = ['_', '_', '_']
        # Creating arrays to check for three marks in a row
        self.first_array = self.first_row  # First row
        self.second_array = self.second_row  # Second row
        self.third_array = self.third_row  # Third row
        self.fourth_array = [self.first_row[0], self.second_row[0], self.third_row[0]]  # First column
        self.fifth_array = [self.first_row[1], self.second_row[1], self.third_row[1]]  # Second column
        self.sixth_array = [self.first_row[2], self.second_row[2], self.third_row[2]]  # Third column
        self.seventh_array = [self.first_row[0], self.second_row[1], self.third_row[2]]  # First diagonal
        self.eighth_array = [self.first_row[2], self.second_row[1], self.third_row[0]]  # Second diagonal

    def win_check_a(self):  # Player a uses 'x's, player b uses 'o's

        def x_count(array):  # Defining a method to count the 'x's in an array
            counter_x = 0
            for k in array:
                if k == 'x':
                    counter_x += 1
            return counter_x

        def o_count(array):  # Defining a method to count the 'o's in an array
            counter_o = 0
            for k in array:
                if k == 'o':
                    counter_o += 1
            return counter_o

        if x_count(self.first_array) == 3:  # Defining cases in which a player wins
            return True
        elif x_count(self.second_array) == 3:
            return True
        elif x_count(self.third_array) == 3:
            return True
        elif x_count(self.fourth_array) == 3:
            return True
        elif x_count(self.fifth_array) == 3:
            return True
        elif x_count(self.sixth_array) == 3:
            return True
        elif x_count(self.seventh_array) == 3:
            return True
        elif x_count(self.eighth_array) == 3:
            return True

        elif o_count(self.first_array) == 3:
            return False
        elif o_count(self.second_array) == 3:
            return False
        elif o_count(self.third_array) == 3:
            return False
        elif o_count(self.fourth_array) == 3:
            return False
        elif o_count(self.fifth_array) == 3:
            return False
        elif o_count(self.sixth_array) == 3:
            return False
        elif o_count(self.seventh_array) == 3:
            return False
        elif o_count(self.eighth_array) == 3:
            return False
        else:
            return

    def draw_check(self):

        def x_count(array):  # Defining a method to count the 'x's in an array
            counter_x = 0
            for k in array:
                if k == 'x':
                    counter_x += 1
            return counter_x

        if x_count(self.first_row) + x_count(self.second_row) + x_count(self.third_row) == 5:  # Player a begins
            return True  # If he set five 'x's and there is no win, it's a draw
        else:
            return False

    def move_a(self, player_input):
        if player_input == 1 and self.first_row[0] == '_':
            self.first_row[0] = 'x'
            self.fourth_array[0] = 'x'
            self.seventh_array[0] = 'x'
        elif player_input == 2 and self.first_row[1] == '_':
            self.first_row[1] = 'x'
            self.fifth_array[1] = 'x'
        elif player_input == 3 and self.first_row[2] == '_':
            self.first_row[2] = 'x'
            self.sixth_array[1] = 'x'
            self.eighth_array[0] = 'x'
        elif player_input == 4 and self.second_row[0] == '_':
            self.second_row[0] = 'x'
            self.fourth_array[1] = 'x'
        elif player_input == 5 and self.second_row[1] == '_':
            self.second_row[1] = 'x'
            self.fifth_array[1] = 'x'
            self.seventh_array[1] = 'x'
            self.eighth_array[1] = 'x'
        elif player_input == 6 and self.second_row[2] == '_':
            self.second_row[2] = 'x'
            self.sixth_array[1] = 'x'
        elif player_input == 7 and self.third_row[0] == '_':
            self.third_row[0] = 'x'
            self.fourth_array[2] = 'x'
            self.eighth_array[2] = 'x'
        elif player_input == 8 and self.third_row[1] == '_':
            self.third_row[1] = 'x'
            self.fifth_array[2] = 'x'
        elif player_input == 9 and self.third_row[2] == '_':
            self.third_row[2] = 'x'
            self.sixth_array[2] = 'x'
            self.seventh_array[2] = 'x'
        else:
            print('This field is not available anymore')
            return 'This fields is not available anymore'

    def move_b(self, player_input):
        if player_input == 1 and self.first_row[0] == '_':
            self.first_row[0] = 'o'
            self.fourth_array[0] = 'o'
            self.seventh_array[0] = 'o'
        elif player_input == 2 and self.first_row[1] == '_':
            self.first_row[1] = 'o'
            self.fifth_array[1] = 'o'
        elif player_input == 3 and self.first_row[2] == '_':
            self.first_row[2] = 'o'
            self.sixth_array[1] = 'o'
            self.eighth_array[0] = 'o'
        elif player_input == 4 and self.second_row[0] == '_':
            self.second_row[0] = 'o'
            self.fourth_array[1] = 'o'
        elif player_input == 5 and self.second_row[1] == '_':
            self.second_row[1] = 'o'
            self.fifth_array[1] = 'o'
            self.seventh_array[1] = 'o'
            self.eighth_array[1] = 'o'
        elif player_input == 6 and self.second_row[2] == '_':
            self.second_row[2] = 'o'
            self.sixth_array[1] = 'o'
        elif player_input == 7 and self.third_row[0] == '_':
            self.third_row[0] = 'o'
            self.fourth_array[2] = 'o'
            self.eighth_array[2] = 'o'
        elif player_input == 8 and self.third_row[1] == '_':
            self.third_row[1] = 'o'
            self.fifth_array[2] = 'o'
        elif player_input == 9 and self.third_row[2] == '_':
            self.third_row[2] = 'o'
            self.sixth_array[2] = 'o'
            self.seventh_array[2] = 'o'
        else:
            print('This field is not available anymore')
            return 'This fields is not available anymore'

    def turn_a(self, player_input):
        self.move_a(player_input)
        print(self.first_row)
        print(self.second_row)
        print(self.third_row)

    def turn_b(self, player_input):
        self.move_b(player_input)
        print(self.first_row)
        print(self.second_row)
        print(self.third_row)


def get_number_a():  # Common method to exclude invalid input
    while True:
        enter = input('Where do you want to place your \'x\'?[1-9] ')
        try:
            enter = int(enter)
            if 0 < enter < 10:
                return enter
            else:
                print('That is no integer between 1 and 9')
        except ValueError:
            print('This is no valid input for an integer')


def get_number_b():
    while True:
        enter = input('Where do you want to place your \'o\'?[1-9] ')
        try:
            enter = int(enter)
            if 0 < enter < 10:
                return enter
            else:
                print('That is no integer between 1 and 9')
        except ValueError:
            print('This is no valid input for an integer')


tic = TicTacToe()

while True:
    tic.turn_a(get_number_a())
    if tic.win_check_a() is True:
        print('Player a won!')
        break
    elif tic.draw_check() is True:
        print('Draw!')
        break
    tic.turn_b(get_number_b())
    if tic.win_check_a() is False:
        print('Player b won!')
        break
