
class Square:
    """
    Class to represent a basic square object
    """

    def __init__(self, side_length):
        """
        Initializer for a square object
        """
        self.set_side_length(side_length)

    def set_side_length(self, side_length):
        """
        Changes the side length of the instance of the square object
        """
        self._length = side_length

    def get_side_length(self):
        """
        Returns the side length of the instance of the square object
        """
        return self._length

    def get_area(self):
        """
        Returns the area of the instance of the square object
        """
        return self._length ** 2

    def __add__(self, other_square):
        """
        Overides the + operator
        The addition of two squares returns a new square with
        a side length equal to the sum of the side lengths of the other squares
        """
        return Square(self.get_side_length() + other_square.get_side_length())

    def __gt__(self, other_square):
        """
        Overides the > operator
        This returns true iff the side length is greater than the other square's
        side length.
        """
        return self.get_side_length() > other_square.get_side_length()

    def __lt__(self, other_square):
        """
        Overides the < operator
        This returns true iff the side length is less than the other square's
        side length.
        """
        return self.get_side_length() < other_square.get_side_length()

    def __eq__(self, other_square):
        """
        Overides the > operator
        This returns true iff the side length is equal to the other square's
        side length.
        """
        return self.get_side_length() == other_square.get_side_length()

    def __ne__(self, other_square):
        """
        Overides the > operator
        This returns true iff the side length is not equal to the other square's
        side length.
        """
        return not (self == other_square)

    def __str__(self):
        """
        Overides the default representation of an instance when it is
        cast to a string.
        """
        square_info = {
            'side_length' : self.get_side_length(),
            'area'        : self.get_area()
            }
        return "Square with side length {side_length} " \
               "and area {area}".format(**square_info)


# This code will only run if we build this module directly
if __name__ == '__main__':
    sq1 = Square(10)
    sq2 = Square(15)
    print(sq1)
    print(sq2)

    print(sq1 + sq2)

    if sq1 != sq2:
        squares = ((str(sq1), str(sq2)), (str(sq2), str(sq1)))[sq1 > sq2]
        print("{0[0]} > {0[1]}".format(squares))

    else:
        print("{0} == {1}".format(sq1, sq2))
