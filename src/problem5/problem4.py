#! /usr/bin/env python
# -*- coding:utf-8 -*-

import itertools


def max_num_combination (num_list) :
    max_num = 0
    for a_list in itertools.permutations(num_list, len(num_list)) :
        num = int(''.join(map(str, a_list)))
        if max_num < num :
            max_num = num
    return max_num


if __name__ == '__main__' :

    num_list = [50, 2, 1, 9]

    print max_num_combination(num_list)
