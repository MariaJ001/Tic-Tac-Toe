
from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def player_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            return False

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
        return random.choice(empty_cells)

    def make_move(self, row, col):
        self.board[row][col] = self.current_player

    def check_game_over(self):
        return self.is_board_full() or self.check_winner('X') or self.check_winner('O')

game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move():
    row = int(request.form['row'])
    col = int(request.form['col'])

    if game.player_move(row, col):
        if game.check_winner('X'):
            return jsonify({'board': game.board, 'winner': 'X'})
        elif game.is_board_full():
            return jsonify({'board': game.board, 'winner': 'tie'})
        else:
            row, col = game.ai_move()
            game.make_move(row, col)
            if game.check_winner('O'):
                return jsonify({'board': game.board, 'winner': 'O'})
            elif game.is_board_full():
                return jsonify({'board': game.board, 'winner': 'tie'})
            else:
                return jsonify({'board': game.board, 'winner': None})
    else:
        return jsonify({'board': game.board, 'message': 'Cell already taken. Try again.'})

if __name__ == "__main__":
    app.run(debug=True)
