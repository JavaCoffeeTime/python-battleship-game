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
    print("\n\n  1 2 3 4 5 6 7 8 9 10")  # Added two newlines before the board
    for i in range(10):
        print(chr(65 + i), end=" ")
        for j in range(10):
            if board[i][j] == 'X':
                print(Fore.RED + board[i][j] + Style.RESET_ALL, end=" ")
            elif board[i][j] == 'O':
                print(Fore.BLUE + board[i][j] + Style.RESET_ALL, end=" ")
            else:
                print(board[i][j], end=" ")
        print()


def place_ship(board, row, col, ship):
    if 0 <= row < 10 and 0 <= col < 10:
        board[row][col] = ship


def main():
    board = init_board()
    # Place the ships
    place_ship(board, 1, 1, 'A')  # Aircraft carrier
    place_ship(board, 0, 3, 'C')  # Cruiser
    place_ship(board, 2, 4, 'D')  # Destroyer
    place_ship(board, 7, 4, 'S')  # Submarine
    place_ship(board, 4, 8, 'T')  # Torpedo boat

    while True:
        print_board(board)
        print("Enter your shot position:")
        shot = input().upper()
        row = ord(shot[0]) - 65
        col = int(shot[1:]) - 1
        if board[row][col] != ' ':
            print("You've touched the ship!")
            board[row][col] = 'X'
        else:
            print("You've missed the ship!")
            board[row][col] = 'O'


if __name__ == "__main__":
    main()
