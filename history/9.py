import random

def game():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        print("\n".join([f"{i+1} | {board[i*3-1]} | {board[i*3]} | {board[i*3+1]}\n---+---+---" for i in range(3)]))

        move = int(input(f"{current_player}'s turn. Which space? (1-9) ")) - 1
        board[move] = current_player

        if check_win(board):
            print("\n".join([f"{i+1} | {board[i*3-1]} | {board[i*3]} | {board[i*3+1]}\n---+---+---" for i in range(3)]))
            print(f"{current_player} wins!")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True
    return False

if __name__ == "__main__":
    game()