#!/usr/bin/env python3

# Global list created before any function definitions
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # gives all of items in the global object my_list unchanged
    return my_list

def give_first_item():
    # gives the first item in the global object my_list as a string
    return my_list[0]

def give_first_and_last_item():
    # gives a  list that includes the first and last items
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    #gives the second and third item
    return [my_list[1], my_list[2]]

if __name__ == '__main__':   # Main block
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
