#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list


my_list = [1,2,3,5,6,7,9,8]
idx = 5
element = 25
result = replace_in_list(my_list, idx, element)
print(result)

