class Square:

    def _set_attributes(self, side):
        self._side = side
        self._perimeter = side * 4
        self._area = side ** 2
        self._diagonal = side * sqrt(2)

    def __init__(self, side):
        self._set_attributes(side=side)

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, new_length):
        self.set_side(new_length)

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, new_length):
        self.set_perimeter(new_length)

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new_area):
        self.set_area(new_area)

    @property
    def diagonal(self):
        return self._diagonal

    @diagonal.setter
    def diagonal(self, new_length):
        self.set_diagonal(new_length)

s1 = Square(2)
s1.side = 6
print(s1.area)