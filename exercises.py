# 🔥 solve with friend help 
class Game:
    def __init__(self):
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.turn = 'X'
        self.winner = None
        self.tie = False




    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
               -----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
               -----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def play_game(self, spot):
        
        if not self.board[spot]:
            self.board[spot] = self.turn
            return True
        else:
            return False

    def check_win(self):
        cols = ["a", "b", "c"]
        
        # Check columns
        for col in cols:
            if self.board[f'{col}1'] == self.turn and self.board[f'{col}2'] == self.turn and self.board[f'{col}3'] == self.turn:
                self.winner = self.turn
                return True

        # Check rows
        for i in range(1, 4):
            if self.board[f'a{i}'] == self.turn and self.board[f'b{i}'] == self.turn and self.board[f'c{i}'] == self.turn:
                self.winner = self.turn
                return True

        # Check diagonals
        if self.board['a1'] == self.turn and self.board['b2'] == self.turn and self.board['c3'] == self.turn:
            self.winner = self.turn
            return True
        if self.board['c1'] == self.turn and self.board['b2'] == self.turn and self.board['a3'] == self.turn:
            self.winner = self.turn
            return True

        return False
# the massag for the welcome and the player turn and the winer in the end of the game 
    def print_message(self):
        print("Welcome player 😎")
        if self.winner:
            print(f"{self.winner} wins the game!")
        elif all(self.board[key] is not None for key in self.board):
            print("It's a tie!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()
# Instantiate the Game class and invoke the play_game method
game_instance = Game()
turns = 0
#  input frome the user ((spot))
while True:
    game_instance.render()
    spot = input("Choose a spot: ")

    if game_instance.play_game(spot):
        if game_instance.check_win():
            game_instance.render()
            break
        game_instance.turn = 'O' if game_instance.turn == 'X' else 'X'
        turns += 1
    else:
        print("choose again.")

    if turns == 9:
        print("It's a tie!")
        break

