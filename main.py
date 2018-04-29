from enum import Enum

class Move(Enum):
    EMPTY = 0
    X = 1
    Y = 2


def get_move(board):
    while True:
        try:
            move = int(input('Where to place the piece (1..9)?\n> '))
            if not (0 < move < 10):
                print('Input must be between 1..9')

            if not board[move] == Move.EMPTY:
                print('Need to choose an empty tile')

            return move
        except ValueError:
            print('Input must be a valid number')

def print_board(board):
   

def main():
    print("Welcome to Aleksander's Tic Tac Toe!")
    board = [Move.EMPTY for _ in range(9)]

    while True:
        move1 = get_move(board)
        print(move1)

    print("Thank's for playing Aleksander's Tic Tac Toe!")
    print("I would like to thank my mentor, Magnus, for great encouragement!")

if __name__ == '__main__':
    main()
