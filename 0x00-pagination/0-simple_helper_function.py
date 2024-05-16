#!/usr/bin/env python3

"""create a function"""


def index_range(page, page_size):
    "The function should return a tuple of size 2"
    index1 = (page -1) * page_size
    index2 = page * page_size

    return(index1, index2)
