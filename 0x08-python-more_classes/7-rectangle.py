#!/usr/bin/python3
''''Task:Write an empty class Rectangle that defines a rectangle'''


class Rectangle():
    '''This is a class that creates instances of a
    rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        area = (self.__width * self.__height)
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        perimeter = ((self.__width * 2) + (self.__height * 2))
        return perimeter

    def __str__(self):
        string = ""
        if self.width == 0 or self.height == 0:
            return string

        for i in range(0, self.height):
            for j in range(0, self.width):
                string += str(self.print_symbol)
            if i != self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
