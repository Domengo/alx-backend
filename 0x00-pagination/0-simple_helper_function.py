#!/usr/bin/env python3
"""function index_range
- params page, page_size
"""


def index_range(page: int, page_size: int) -> tuple:
    '''return  tuple'''
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return start_idx, end_idx
