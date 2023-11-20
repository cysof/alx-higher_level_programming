#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count

# Example usage:
my_list = [1, 2, 3, 4, 5]
elements_printed = safe_print_list(my_list, 3)
print("Number of elements printed:", elements_printed)

