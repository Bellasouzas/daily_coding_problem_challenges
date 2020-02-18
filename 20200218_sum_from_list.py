# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 07:11:29 2020

@author: laion

This challenge was presented by e-mail distribution at 02/18/20
by https://www.dailycodingproblem.com .

The challenge description is:
    Given a list of numbers and a number k, return whether
    any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17,
    return true since 10 + 7 is 17.
"""


# This function adds up items in a list and finds if a number is on that result list.
def sum_from_list(k: 'int or float' = 0, ls: 'list' = []) -> 'bool':
    """
    Add items in a list and finds if a number is on that result list.

    Description
        Adds up all the elements combinatios on a list ls of ints of
        ints or floats and compares with a int or float k.
        If k is in ls summed list, returns True, else False.

    Arguments
    ---------
        - k: int or float, = 0
        - ls: list of ints and/or floats, =[]

    Returns
    -------
        - True or False. If arguments are missing, returns False.
    """
    assert isinstance(k, (int, float)), 'The first parameter needs to be an int or a float'
    assert isinstance(ls, list), 'The second parameter needs to be a list'
    assert all(isinstance(x, (int, float)) for x in ls), ' All the elements in list ls need to be int of float types'
    i = 0
    j = 1
    mapped = []
    while i < len(ls):
        while j < len(ls):
            mapped.append(ls[i] + ls[j])
            j += 1
        i += 1
        j = i + 1
    return True if k in mapped else False


"""
***TESTS***

# k empty
print(sum_from_list([1,2,3]))

# k is an string
print(sum_from_list("a", [1,2,3]))

# k is a list
print(sum_from_list([1,2,3], [1,2,3]))

# k in a dict
print(sum_from_list({"a":0}, [1,2,3]))

# ls empty
print(sum_from_list(3))

# ls contains a string
print(sum_from_list(3, [1,2,"a"]))

# ls contains a list
print(sum_from_list(3, [1,2,[1,2,3]]))

# ls contains a dict
print(sum_from_list(3, [1,2,{"a":0}]))

# k and ls empty
print(sum_from_list())
"""
