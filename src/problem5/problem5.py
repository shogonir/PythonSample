#! /usr/bin/env python
# -*- coding:utf-8 -*-

import itertools
from problem2 import combine_alternately


if __name__ == '__main__' :

    operations = ['+', '-', '']

    for string in itertools.product(operations, repeat=8) :

        num_list = ['{0}'.format(i+1) for i in range(9)]
        formula = ''.join(combine_alternately(num_list, string))

        if eval(formula) == 100 :
            print formula, '=', eval(formula)
