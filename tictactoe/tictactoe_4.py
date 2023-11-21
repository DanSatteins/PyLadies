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
    if position <= 19 and position >= 0:
        if board[position] == "-":
            new_board = ""
            for i in range(0, 19):
                if i == position:
                    new_board = board + mark
                else:
                    new_board = board + board[i]
            return new_board
        else:
            print("You can not place your mark here, please try again.")
    else:
        print("Please check your entry!")

        return board
   

# Step 3. I have to admitt that I got some support here.

def player_move(board, mark):  
    while True:
        position = int(input("Please enter the desired position from 0 to 19: "))
        if position <= 19 and position >= 0:
        mark = "x"
    
    if position <= 19 and player_move >= 0:
        if board[player_move] == "-":
            board[player_move] = "x"
            return(board)
        else:
            print("You can not place your mark here, please try again.")
    else:
        print("Please check your entry!")
    
# Step 4

def pc_move(board):  
    
while evaluate(board) != "-":
    print(board)
    pc_move = randrange(0, 19)
    if board[pc_move] == "-":
        board[pc_move] == "o"
    else:
        pc_move
        
board = 

    
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