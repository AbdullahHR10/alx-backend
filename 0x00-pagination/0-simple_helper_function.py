#!/usr/bin/env python3
""" Module that contains the index_range function. """


def index_range(page: int, page_size: int) -> tuple:
    """ Calculates the start and end indexes for pagination. """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
