#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    len = 0
    
    #finding the actual length of the given list
    
    for num in my_list:
        len += 1
        
    if (x > len):
        raise IndexError
        
    for i in range (0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            
            count += 1
            
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count