from move_ttt import move

def test_move_ttt_x():
    board = "---x-x----oxoxoxoxox"
    mark = "x"
    position = 4
    new_board = board[:position] + mark + board[position+1:]
    assert new_board == "---xxx----oxoxoxoxox"
    
def test_move_ttt_o():
    board = "---x-x----o-oxoxoxox"
    mark = "o"
    position = 11
    new_board = board[:position] + mark + board[position+1:]
    assert new_board == "---x-x----oooxoxoxox"

def test_move_ttt_err():
    board = "---x-x----o-oxoxoxox"
    mark = "o"
    position = 21
    new_board = board[:position] + mark + board[position+1:]
    assert new_board == "---x-x----o-oxoxoxox"
    
# What is a Python module and how does it differ from a Python package? - A Python module is a collection of functions,
# classes, etc which helps to organize your code. Modules can be imported to and used by other modules. 
# A Python package contains multiple modules. It may have severel levels of sub-packages, import works just as for modules.

# What are side effects and give some examples. - This is when a module does not simply return a value but prints or changes
# something within itself or in the whole program. E.g., a varible is changed, something is printed, data is added in the
# original data/list/dictionary, another function is called. Side effects are not always negative, but should be avoided 
# because they might cause bugs.

# What are Exceptions and what to do if third-party code that we use throws them? - An exception is an error message.
# These occur if the code cannot be executed as expected and give hints to where the problem might be (where, what). In 
# Python, "raise" raises exceptions. In Python, there are many standard exceptions organized in a hierarchy.
# 3rd pary code - do not test the 3rd pary code itself in your unit test or use a test suite for it, log exceptions but 
# don't abort your program.

# Using which keywords can you create, throw and catch your new custom Exception? - Create = "exception", throw = "raise", 
# catch = "try", "except".

# Give examples of some benefits of testing? - Make sure the code runs as expected, that it handles input error and edge-
# cases, find bugs early (at least before the software is with the customer), find errors early (little complexity), 
# enhance code quality, avoid disappointed customers and damage claims, ....
 