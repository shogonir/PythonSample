#! /usr/bin/env python
# -*- coding:utf-8 -*-


def combine_alternately (list1, list2) :
    new_list = []
    i, j = 0, 0
    while i < len(list1) or j < len(list2) :
        if i < len(list1) :
            new_list.append(list1[i])
        if j < len(list2) :
            new_list.append(list2[j])
        i += 1
        j += 1
    return new_list


if __name__ == '__main__' :

    list1, list2 = ['1', '2', '3', '4'], ['a', 'b', 'c']

    print combine_alternately(list1, list2)
