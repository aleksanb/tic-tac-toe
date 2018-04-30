from enum import Enum

class Move(Enum):
    EMPTY = 0
    X = 1
    O = 2

    def __str__(self):
        if self == Move.EMPTY:
            return " "
        elif self == Move.X:
            return "X"
        else:
            return "O"


def process_move(board, marker):
    while True:
        try:
            move = int(input('Where to place the piece (1..=9)?\n> '))
            if not (1 <= move <= 9):
                print('Input must be between 1..=9')
                continue

            if not board[move - 1] == Move.EMPTY:
                print('Need to choose an empty tile')
                continue

            board[move - 1] = marker
            break
        except ValueError:
            print('Input must be a valid number')

def check_game_over(board):
    for i in range(3):
        # Check horizontals
        if (board[i*3] == board[i*3 + 1] == board[i*3 + 2]) and board[i*3] != Move.EMPTY:
            return True
        # Check verticals
        if board[i] == board[i + 3] == board[i + 6] and board[i] != Move.EMPTY:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] and board[0] != Move.EMPTY:
        return True
    if board[2] == board[4] == board[6] and board[2] != Move.EMPTY:
        return True

    return False

def print_board(board):
    print('[{}] [{}] [{}]'.format(board[0], board[1], board[2]))
    print('[{}] [{}] [{}]'.format(board[3], board[4], board[5]))
    print('[{}] [{}] [{}]'.format(board[6], board[7], board[8]))

def main():
    print("Welcome to Aleksander's Tic Tac Toe!")

    board = [Move.EMPTY for _ in range(9)]
    print_board([i for i in range(1, 10)])

    num_moves = 0

    while True:
        # Player 1
        process_move(board, Move.X)
        print_board(board)

        if check_game_over(board):
            print("Player X won!")
            break

        num_moves += 1
        if num_moves == 9:
            print("The game seems to be a draw!")
            break

        # Player 2
        process_move(board, Move.O)
        print_board(board)

        if check_game_over(board):
            print("Player O won!")
            break

        num_moves += 1
        if num_moves == 9:
            print("The game seems to be a draw!")
            break

    print("Thank's for playing Aleksander's Tic Tac Toe!")
    print("I would like to thank my mentor, Magnus, for great encouragement!")

if __name__ == '__main__':
    main()
