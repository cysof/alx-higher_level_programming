#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new_dic = a_dictionary
        new_dic[key] = value
        return new_dic
