#! /usr/bin/env python
# -*- coding:utf-8 -*-


def sum_using_for(num_list) :
    list_sum = 0
    for num in num_list :
        list_sum += num
    return list_sum


def sum_using_while(num_list) :
    list_sum, i = 0, 0
    while i < len(num_list) :
        list_sum += num_list[i]
        i += 1
    return list_sum


def sum_using_recursive(num_list, i=0) :
    if i == len(num_list) - 1 :
        return num_list[i]
    else :
        return num_list[i] + sum_using_recursive(num_list, i+1)


if __name__ == '__main__' :

    number_list = range(10)

    print 'list_sum using for loop           :', sum_using_for(number_list)
    print 'list_sum using while loop         :', sum_using_while(number_list)
    print 'list_sum using recursive function :', sum_using_recursive(number_list)
