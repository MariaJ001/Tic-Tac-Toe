import random

def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if a player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for row in board for cell in row)

def player_move(board):
    """Prompts the player to enter their move."""
    while True:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            return row, col
        else:
            print("Cell already taken. Try again.")

def minimax(board, depth, is_maximizing):
    """Implements the minimax algorithm to determine the best move for the AI."""
    if check_winner(board, 'X'):
        return -10
    elif check_winner(board, 'O'):
        return 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    """Determines the best move for the AI using the minimax algorithm."""
    best_score = -float('inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

def play_tic_tac_toe():
    """Plays the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row, col = player_move(board)
        else:
            print("AI is making a move...")
            row, col = ai_move(board)

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
