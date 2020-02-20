# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:22:24 2020

@author: laion

This challenge was presented by e-mail distribution at 02/18/20
by https://www.dailycodingproblem.com .

The challenge description is:
    Given an array of integers, return a new array such that each element
    at index i of the new array is the product of all the numbers in the
    original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5],
    the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

from functools import reduce


def leave_me_out(ls: 'list' = []) -> 'list':
    """
    Get some list ls and build another list result where the element result[i] will be the product of all the elements of ls, except ls[i].

    Description
        Given a list of numbers, it builds another list where each element will be
        the product of all elements of the original list, except the element with
        the same index.

    Parameters
    ----------
        ls : 'list', optional.
            DESCRIPTION. A list of numbers. The default is [].

    Returns
    -------
        result : 'list'.
            DESCRIPTION. A list of numbers with the same lenght of the
            original list.
    """

    assert isinstance(ls, list), 'You need to pass a list of numbers as argument'
    assert all(isinstance(x, (int)) for x in ls), 'All the elements in list ls needs to be int type'

    result = []
    for i in range(len(ls)):
        ls_copy = ls[:]
        del ls_copy[i]
        result.append(reduce(lambda x, y: x * y, ls_copy))
    return result

"""
***TESTS***

# ls is empty -> Runs, returns None
print(leave_me_out())

#ls is not a list -> exception
print(leave_me_out((1,2,3)))

# ls contains floats -> Runs. Returns a list
print(leave_me_out([1,2,3.1]))

#ls contains strings -> exception
print(leave_me_out([1,2,"a"]))

# ls contais lists -> exception
print(leave_me_out([1,2,[1,2,3]]))
"""
