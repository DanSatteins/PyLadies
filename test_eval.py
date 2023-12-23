from eval import evaluate

def test_eval_x():
    result_move = evaluate("---xxx----oxoxoxoxox")
    assert result_move == "x"
    
def test_eval_o():
    result_move = evaluate("---ooo----oxoxoxoxox")
    assert result_move == "o"
    
def test_eval_draw():
    result_move = evaluate("xoxoxoxoxxoxoxoxoxox")
    assert result_move == "!"
    
def test_eval_play():
    result_move = evaluate("xoxox---xxoxoxoxoxox")
    assert result_move == "-"

def test_eval_err():
    result_move = evaluate("---xxx----oxoxoxoxox")
    assert result_move == "!"
    
def test_eval_empty():
    result_move = evaluate("")
    assert result_move == "!"

def test_eval_empty_2():
    result_move = evaluate("")
    assert result_move == "-"