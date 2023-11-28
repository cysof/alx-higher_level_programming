#!/urs/bin/python3

class Rectangle:
    """ Rectangle Class """

    def __init__(self, width=0, height=0):
        """ __init__ method.
        Args:
            width (ini): integer width
            height (init: integer height
            """
            self.width = width
            self.height =height
        @property
        """ property Decorrector """
        def width(self):
            """width: returns width
            Args:
                width (int): integer width
            Returns:
                Rectangle width
            Raises:
                TypeError: if width is not an integer
                ValueError: if width is less 0
            """
            return self.__height

        @width.setter
        def width(self, width):
            if not isintance(width, int):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
             @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
