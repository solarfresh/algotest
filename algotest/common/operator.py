# -*- coding: utf-8 -*-


def multiply_three_point_five(x):
    # To calculate 2*x, left shift x by 1 and to calculate x/2, right shift x by 2.
    return (x << 1) + x + (x >> 1)
