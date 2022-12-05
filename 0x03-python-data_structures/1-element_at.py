#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 and idx > len(my_list) - 1:
        return None
    for i in range(idx):
        element = my_list[i + 1]
    return element
