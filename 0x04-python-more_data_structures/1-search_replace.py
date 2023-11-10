#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = []
        for i, n in enumerate(my_list):
            if my_list[i] == search:
                new_list.append(replace)
            else:
                new_list.append(my_list[i])
        return new_list`
