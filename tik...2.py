import openai
from stringcolor import * # for color, importing stringcolor library

openai.api_key = "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" # api key
model 	       = "gpt-3.5-turbo" # choosing gpt model

role ="""
    You are the users opponent in the game Tik Tak Toe.
    
    You have to respond only with the position of your move.
    
    You use a O, while the player uses a X  
    
    The Board is defined as a square 3 x 3, where every row is associated
    to a letter (from top to bottom A is the first and C is on the last)
    and every column to a number (from left to right 1 is the first and 3).
        
    The game ends as soon you or the player have 3 of their own symbols (O
    for you, X for the player) in one of the three rows, one of the three
    columns or one of the two diagonals. 
    """ 
# finish and test prompt for gpt
# make sure its output can be used for game logic
# make sure it knows how the board looks
# maybe give it your code as input?
# maybe board.board not in role but in user_input?

class TikTakToe: # Playing against AI in TTT
    def __init__(self):
        self.role = role

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
            {"role": "system", "content": self.role},
            {"role": "user", "content": user_input},]
        )
        result = response.choices[0].message.content
        return result


bot = TikTakToe()

# loop here? for game logic?

class Board:
    def __init__(self):
        self.board = {"A": [" "," "," "],
                      "B": [" "," "," "],
                      "C": [" "," "," "]}

class Game:
    def __init__(self):
        self.board = Board()
        self.field = self.board.board

    def display_board(self):
        print("    1   2   3  ")
        print(f"A   {self.field['A'][0]}   {self.field['A'][1]}   {self.field['A'][2]}")
        print(f"B   {self.field['B'][0]}   {self.field['B'][1]}   {self.field['B'][2]}")
        print(f"C   {self.field['C'][0]}   {self.field['C'][1]}   {self.field['C'][2]}")
    
    def make_move(self, who):
        print(
            """Choose a square
            1, 2, 3
            4, 5, 6
            7, 8, 9""")
        square = int(input(""))
        
        if square in range(1, 10):
            if self.field[num] == " ":
                self.field[num] = square
            else:
                print("nah")
        else:
            print("nah man error, invalid move")
        
    def check_win(self, who):
        win_cases = {
            "case1":[ self.field["A"][0] == who,
                      self.field["B"][1] == who,
                      self.field["C"][2] == who],
            "case2":[ self.field["A"][2] == who,
                      self.field["B"][1] == who,
                      self.field["C"][0] == who],
            "case3":[ self.field["A"][0] == who,
                      self.field["B"][0] == who,
                      self.field["C"][0] == who],
            "case4":[ self.field["A"][1] == who,
                      self.field["B"][1] == who,
                      self.field["C"][1] == who],
            "case5":[ self.field["A"][2] == who,
                      self.field["B"][2] == who,
                      self.field["C"][2] == who],
            "case6":self.field["A"] == [who,who,who],
            "case7":self.field["B"] == [who,who,who],
            "case8":self.field["C"] == [who,who,who]
        }
        print(win_cases["case1"])
        print(win_cases["case6"])
        """if win_cases["case1"] == [True,True,True]:
            # player wins"""

game = Game()

game_loop = True
while game_loop == True:
    game.display_board()
    game.make_move("X")
    game.check_win("X")