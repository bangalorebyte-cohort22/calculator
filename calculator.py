#!/usr/bin/env python3

''' Calculator app '''

def user_input():
    user_input = input("Enter your maths operation and numbers: ")
    return user_input.split(" ")

def input_check(user_input):
    if len(user_input)!=3:
        print("Please enter either: div, mul, add, sub and 2 numbers separated with spaces")
        raise "Error"
    # if user_input[1] == str.__contai
    if "." in user_input[1] and user_input[2]:
        print ("Not a whole number. Please enter a whole number.")
    # if user_input
    # user_input[0] in ['div', 'mul', 'add', 'sub']


def add():
    pass

def subtract():
    pass

def multiply():
    pass

def divide():
    pass



- len
- specific Error
- element 2 or 3 must be whole
