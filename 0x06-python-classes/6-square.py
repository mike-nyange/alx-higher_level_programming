#!/usr/bin/python3

"""class Square that defines a square by size"""


class Square:
    """Initiating an instance of the class"""

    def __init__(self, size=0):
        if not (type(size) == int):
            raise TypeError('size must be an integer')
        if(size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size

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
        
        
    def my_print(self):
        
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="\n" if j is self.__size -1 and i != j else "")
        print()