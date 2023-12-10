# One-dimensional Tic-Tac-Toe game with random function for pc-player

from random import randrange

# Step 1 - definition of szenarios

def evaluate(board):
  board_str = "".join(board)
  if "xxx" in board_str:
    print(board)
    result_move = "x"
    print("Congrats, the player has won!")
  elif "ooo" in board_str:
    print(board)
    result_move = "o"
    print("Oh no, the pc has won!")
  elif "-" not in board_str:
    print(board)
    result_move = "!"
    print("Draw!")
  else:
    result_move = "-"
    print("Play!")
  return result_move


# Step 2 - not needed

# Step 3

def player_move(board):
  position = int(input("Please enter the desired free position from 0 to 19: "))
  if position >= 0 and position <= 19:
    if board[position] == "-":
      board[position] = "x"
    else:
      print("You can not place your mark here, please try again.")
      player_move(board)
  else:
    print("Please check your entry!")
    player_move(board)
  return position

# Step 4

def pc_move(board):
  position = randrange(0, 19)
  if board[position] == "-":
    board[position] = "o"
  else:
    pc_move(board)
  return position

# Step 5

def tictactoe():
  board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
  turn = 1
  result = evaluate(board)

  while result == "-":
    print(board)
    if turn == 1:
      player_move(board)
      turn = turn * -1
      result = evaluate(board)
    else:
      pc_move(board)
      turn = turn * -1
      result = evaluate(board)

tictactoe()