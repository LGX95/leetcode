#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""help function
"""

__author__ = 'lgx'
__date__ = '2020-10'

import inspect


def print_vars(*args):
    """print variable names and their value
    """
    frame = inspect.currentframe()
    variables = {}
    for i in args:
        for k, v in frame.f_back.f_locals.items():
            if i is v:
                variables[k] = v

    print(', '.join(f'{k}: {v}' for k, v in variables.items()))


if __name__ == '__main__':
    s = 'hello'
    l = ['hello', 'world']
    i = 123
    print_vars(s, l, i)
