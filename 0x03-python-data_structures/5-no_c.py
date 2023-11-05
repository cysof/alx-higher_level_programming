#!/usr/bin/python3

def no_c(my_string):
    output = []
    for char in my_string:
        if char != 'c' and char !='C':
            output.append(char)
    return ''.join(output)
