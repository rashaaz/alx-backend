#!/usr/bin/env python3
'''
    Module for pagination
'''


def index_range(page, page_size):
    '''
        Returns tuple: A tuple containing
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
