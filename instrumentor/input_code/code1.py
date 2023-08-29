def something(a):
    return a
    
def sum(a,b):
    return a + b

def div(a,b):
    return a/b


def test_sum():
    assert sum(2,3) == 5, "Should be 5"
def test_sum_tuple():
    assert sum( 3, 7) == 10 , "Should be 10"


test_sum()
test_sum_tuple()

