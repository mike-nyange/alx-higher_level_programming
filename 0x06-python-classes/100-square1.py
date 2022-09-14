#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.__data = data
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value
        
    @property
    def next_node(self):
        pass
    
    @next_node.setter
    def next_node(self, value):
        pass

