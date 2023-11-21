# One-dimensional Tic-Tac-Toe game with random function for pc-player

from random import randrange

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
    evaluate = "-"
    print("Continue")
  return evaluate)

# print(evaluate(board))

# Step 2
    
def move(board, mark, position):
    if position >= 0 and position <= 19:
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
    print(board)
    position = int(input("Please enter the desired position from 0 to 19: "))
    
    if position <= 19 and position >= 0:
        if board[position] == "-":
            mark = "x"
        else:
            print("You can not place your mark here, please try again.")
            player_move(board, mark)
    else: 
        print("Please check your entry!")
        player_move(board, mark)
    
        return mark
    return position

# Step 4

def pc_move(board, mark):
    position = randrange(0, 19)
    if board[position] == "-":
        mark = o
    else:
        pc_move(board, mark)
    
# Step 5

def 1d_tictactoe:
    board = "-" * 20

    while evaluate(board) != "!":  
        player_move(boar, mark)
        pc_move(board, mark)
        move(board, mark, position)    
        evaluate(board)
        print(board)