# One-dimensional Tic-Tac-Toe game with random function for pc-player

from random import randrange

# Step 1 - definition of szenarios

def evaluate(board, result):
  board = "-" * 20
  if "xxx" in board:
    result = "x"
    print("Congrats, the player has won!")
  elif "ooo" in board:
    result = "o"
    print("Oh no, the pc has won!")
  elif "-" not in board:
    result = "!"
    print("Draw!")
  else:
    result = "-"
    print("Continue")
  return result

# print(result) - I wanted to verify the returned result when trying

# Step 2 - I have to admitt that I got some support here.

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
        board = new_board
        return board


# Step 3

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
        mark = "o"
    else:
        pc_move(board, mark)

# Step 5

def tictactoe(player_move, pc_move):
# ?  board = "-" * 20
    turn = 1

    while result != "!":
      print(board)
      if turn == 1:
        mark = "x"
        player_move(board, mark)
        turn = turn * -1
        move(board, mark, position)
        print(board)
        return mark
      else:
        mark = "o"
        pc_move(board, mark)
        turn = turn * -1
        return mark
      move(board, mark, position)
      print(board)

tictactoe(player_move, pc_move)