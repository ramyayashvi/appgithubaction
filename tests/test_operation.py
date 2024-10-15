from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(0,1)==0

def test_sub():
    assert sub(6,0)==6
    assert sub(7,6)==1