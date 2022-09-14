#!/usr/bin/python3

"""class Square that defines a square by size"""


class Square:
    """Initiating an instance of the class"""

    def __init__(self, size=0, position=(0, 0)):
        if not (type(size) == int):
            raise TypeError('size must be an integer')
        if(size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size        
        self.__position = position

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (type(value) == int):
            raise TypeError('size must be an integer')
        if(value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value
        
    @property
    def position(self):
        return self.__position

    @position.setter
    def size(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be tuple of 2 positive integers")

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            i, j = 0, 0
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(" " * self.__position[0], "#" * self.__size))
        
    
