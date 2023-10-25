#!/usr/bin/env python
# -*- coding: utf-8 -*-
from colorama import Fore, Style


def init_board():
    board = []
    for i in range(10):
        board_row = []
        for j in range(10):
            board_row.append(' ')
        board.append(board_row)
    return board


def print_board(board):
    print("\n\n  A B C D E F G H I J")
    for i in range(10):
        print(i+1, end=" ")
        for j in range(10):
            if board[j][i] == 'X':
                print(Fore.RED + board[j][i] + Style.RESET_ALL, end=" ")
            elif board[j][i] == 'O':
                print(Fore.BLUE + board[j][i] + Style.RESET_ALL, end=" ")
            else:
                print(board[j][i], end=" ")
        print()


def place_ship(board, start_row, start_col, end_row, end_col, ship):
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            board[j][i] = ship


def main():
    board = init_board()
    place_ship(board, 1, 1, 1, 5, 'A')  # Aircraft carrier
    place_ship(board, 3, 0, 6, 0, 'C')  # Cruiser
    place_ship(board, 4, 2, 6, 2, 'D')  # Destroyer
    place_ship(board, 4, 7, 4, 9, 'S')  # Submarine
    place_ship(board, 8, 4, 8, 5, 'T')  # Torpedo boat

    while True:
        print_board(board)
        print("Enter your shot position:")
        shot = input().upper()
        user_input = {'col': ord(shot[0]) - 65, 'row': int(shot[1:]) - 1}
        if board[user_input['col']][user_input['row']] != ' ':
            print("You've touched the ship!")
            board[user_input['col']][user_input['row']] = 'X'
        else:
            print("You've missed the ship!")
            board[user_input['col']][user_input['row']] = 'O'


if __name__ == "__main__":
    main()
