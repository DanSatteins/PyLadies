# One-dimensional Tic-Tac-Toe game with random function for pc-player

from random import randrange

board = ("--------------------")
print(board)

# Step 1

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
  return evalutae(board)

print(evaluate(board))

# Step 2
    
def move(board, mark, position):
    
    
    
while evaluate(board) != "-":
    print(board)
    pc_move = randrange(0, 19)
    if board[pc_move] == "-":
        board[pc_move] == "o"
    else:
        pc_move
        
board = 
player_move = int(input("Please place your mark in position 0 to 19: "))
    
    while
    
    
def pc_move(board):
    
    
def yes_or_no(question):
    "Returns True or False, depending on the user's answers."
    while True:
        answer = input(question)
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print('What do you want!! Just  type "Yes" or "No".')

if yes_or_no('Do you want to play a game?'):
    print('OK, but you have to program it first.')
else:
    print('That is sad.' )
    
    
    def explore(depth):
     print(f'Looking around at a depth of {depth} m')
     if depth >= 30:
         print('Enough! I have seen it all!')
     else:
         print(f'I dive more (from {depth} m)')
         explore(depth + 10)
         print(f'Surfacing (at {depth} m)')