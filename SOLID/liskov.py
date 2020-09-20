class Rectangle:
    def __init__(self, width, height):
            self._height = height
            self._width = width

    @property
    def area(self):
        return self._width * self._height

    @property
    def is_square(self):
        return bool(self._height == self._width)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected area of {expected}, got {rc.area}')
    print(f'Rectangle is a square? {rc.is_square}')

if __name__ == '__main__':
    rc = Rectangle(10, 10)
    use(rc)


class Calculator:
    def calculate(self, a, b): # returns a number
        return a * b

class DividerCalculator(Calculator):
    def calculate(self, a, b): # returns a number or raises an Error
        return a / b

calculation_results = [
    Calculator().calculate(3, 4),
    Calculator().calculate(5, 7),
    DividerCalculator().calculate(3, 4),
    DividerCalculator().calculate(5, 0) # 0 will cause an Error
]

print(calculation_results)