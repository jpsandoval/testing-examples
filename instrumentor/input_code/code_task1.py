from math import hypot

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return hypot(dx, dy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Point (%s, %s)"%(self.x, self.y)


def test_str():
    point = Point(7, 10)
    assert point.__str__() == 'Point (7, 10)', 'Incorrect output'

def test_compare1():
    point1 = Point(5, 13)
    point2 = Point(19, 72)
    assert point1 != point2, 'Different points'

def test_compare2():
    point1 = Point(2, 3)
    point2 = Point(5, 3)
    assert point1 != point2, 'Different points'

def test_compare3():
    point1 = Point(22, 45)
    point2 = Point(22, 27)
    assert point1 != point2, 'Different points'

def test_compare_equal():
    point1 = Point(2, 5)
    point2 = Point(2, 5)
    assert point1 == point2, 'Equal points'


test_str()
test_compare1()