import math

class Circle:
    """
    Class to represent a basic circle object
    """

    def __init__(self, radius):
        """
        Initializer for a circle object
        """
        self.set_radius(radius)

    def set_radius(self, radius):
        """
        Changes the radius of the instance of the circle object
        """
        self._radius = radius

    def get_radius(self):
        """
        Returns the radius of the instance of the circle object
        """
        return self._radius

    def get_area(self):
        """
        Returns the area of the instance of the circle object
        """
        return math.pi * (self._radius ** 2)

    def __add__(self, other_circle):
        """
        Overides the + operator
        The addition of two circles returns a new circle with
        a radius equal to the sum of the radiuss of the other circles
        """
        return Circle(self.get_radius() + other_circle.get_radius())

    def __gt__(self, other_circle):
        """
        Overides the > operator
        This returns true iff the radius is greater than the other circle's
        radius.
        """
        return self.get_radius() > other_circle.get_radius()

    def __lt__(self, other_circle):
        """
        Overides the < operator
        This returns true iff the radius is less than the other circle's
        radius.
        """
        return self.get_radius() < other_circle.get_radius()

    def __eq__(self, other_circle):
        """
        Overides the > operator
        This returns true iff the radius is equal to the other circle's
        radius.
        """
        return self.get_radius() == other_circle.get_radius()

    def __ne__(self, other_circle):
        """
        Overides the > operator
        This returns true iff the radius is not equal to the other circle's
        radius.
        """
        return not (self == other_circle)

    def __str__(self):
        """
        Overides the default representation of an instance when it is
        cast to a string.
        """
        circle_info = {
            'radius'      : self.get_radius(),
            'area'        : self.get_area()
            }
        return "circle with radius {radius} " \
               "and area {area}".format(**circle_info)


# This code will only run if we build this module directly
if __name__ == '__main__':
    c1 = Circle(10)
    c2 = Circle(15)
    print(c1)
    print(c2)

    print(c1 + c2)

    if c1 != c2:
        circles = ((str(c1), str(c2)), (str(c2), str(c1)))[c1 > c2]
        print("{0[0]} > {0[1]}".format(circles))

    else:
        print("{0} == {1}".format(c1, c2))
