import math
import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'
        self.computer = 'O'

    def print_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[i*3], '|', self.board[i*3 + 1], '|', self.board[i*3 + 2], '|')
            print('-------------')

    def is_board_full(self):
        return ' ' not in self.board

    def is_winner(self, player):
        return ((self.board[0] == player and self.board[1] == player and self.board[2] == player) or
                (self.board[3] == player and self.board[4] == player and self.board[5] == player) or
                (self.board[6] == player and self.board[7] == player and self.board[8] == player) or
                (self.board[0] == player and self.board[3] == player and self.board[6] == player) or
                (self.board[1] == player and self.board[4] == player and self.board[7] == player) or
                (self.board[2] == player and self.board[5] == player and self.board[8] == player) or
                (self.board[0] == player and self.board[4] == player and self.board[8] == player) or
                (self.board[2] == player and self.board[4] == player and self.board[6] == player))

    def player_move(self):
        while True:
            move = input("Enter your move (0-8): ")
            try:
                move = int(move)
                if move >= 0 and move <= 8:
                    if self.board[move] == ' ':
                        self.board[move] = self.player
                        break
                    else:
                        print("This cell is already occupied!")
                else:
                    print("Enter a number within the range!")
            except:
                print("Enter a valid integer!")

    def computer_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.computer
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = self.computer

    def minimax(self, maximizing):
        if self.is_winner(self.player):
            return -1
        elif self.is_winner(self.computer):
            return 1
        elif self.is_board_full():
            return 0
        elif maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.computer
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.player
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(best_score, score)
            return best_score


    def play(self):
        print("Tic Tac Toe game!")
        print("*****************")
        self.print_board()
        print("You are playing as 'X' against the computer as 'O'.")
        print("Enter a number (0-8) to make a move.")

        while not self.is_board_full():
            self.player_move()
            self.print_board()
            if self.is_winner(self.player):
                print("Congratulations, you won!")
                return
            elif self.is_board_full():
                print("It's a tie!")
                return
            print("Computer is thinking...")
            self.computer_move()
            self.print_board()
            if self.is_winner(self.computer):
                print("Sorry, you lost!")
                return
            elif self.is_board_full():
                print("It's a tie!")
                return

game = TicTacToe()
game.play()
