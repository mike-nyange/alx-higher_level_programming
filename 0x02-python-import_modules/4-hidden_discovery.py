#!/usr/bin/python3
from sys import argv
import hidden_4

if __name__ == "__main__":
    # all_dir = dir(hidden_4)
    # for i in range(0, len(all_dir)):
    #     if "__" != all_dir[i][:2]:
    #         print(all_dir[i])
    for arg in dir(hidden_4):
        if arg[:2] != "__":
            print("{}".format(arg))
