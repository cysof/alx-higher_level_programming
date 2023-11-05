#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for rw in matrix:
        for i, num in enumerate(rw):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
