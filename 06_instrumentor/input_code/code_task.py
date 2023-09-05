class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


def test_area():
    rectangle = Rectangle(2, 3)
    assert rectangle.get_area() == 6, 'Incorrect area'

def test_perimeter():
    rectangle = Rectangle(5, 7)
    assert rectangle.get_perimeter() == 24, 'Incorrect perimeter'

def test_compare1():
    rectangle1 = Rectangle(2, 3)
    rectangle2 = Rectangle(5, 7)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare2():
    rectangle1 = Rectangle(2, 3)
    rectangle2 = Rectangle(5, 3)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare3():
    rectangle1 = Rectangle(2, 5)
    rectangle2 = Rectangle(2, 7)
    assert rectangle1 != rectangle2, 'Different rectangles'

def test_compare_equal():
    rectangle1 = Rectangle(2, 5)
    rectangle2 = Rectangle(2, 5)
    assert rectangle1 == rectangle2, 'Equal rectangles'


test_area()
test_perimeter()
test_compare1()
test_compare2()
test_compare3()
test_compare_equal()