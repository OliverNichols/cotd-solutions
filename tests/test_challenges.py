from programs.solution_1 import alphasort
from programs.solution_2 import fibonacci
from programs.solution_3 import even_digits

def test_alphasort():
    assert alphasort("hello world and hello again") == "again and hello world"
    assert alphasort("passing some gibberish") == "gibberish passing some"
    assert alphasort("5 4 3 2 1 blastoff") == "1 2 3 4 5 blastoff"

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(0) == 0

def test_even_digits():
    assert even_digits(10, 30) == "20,22,24,26,28"
    assert even_digits(1,100) == "2,4,6,8,20,22,24,26,28,40,42,44,46,48,60,62,64,66,68,80,82,84,86,88"
