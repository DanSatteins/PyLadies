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
