# One-dimensional Tic-Tac-Toe game with random function for pc-player

from random import randrange

board = ("--------------------")
print(board)

def evaluate(board):  
  if "xxx" in board:
    evaluate = "x"
    print("Congrats, the player has won!")
  elif "ooo" in board:
    evaluate = "o"
    print("Oh no, the pc has won!")
  elif "-" not in board:
    evaluate = "!"
    print("Draw!")
  else:
    evalutae = "-"
    print("Continue")
  return evalutae

print(evaluate(board))
    
def move(board, mark, position):
    while
    
    
def pc_move(board):
    
    
        pc_move = randrange(0, 19)
    player_move = int(input("Please place your mark in position 1 to 20: "))