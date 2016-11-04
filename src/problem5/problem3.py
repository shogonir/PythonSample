#! /usr/bin/env python
# -*- coding:utf-8 -*-


def fibonacci_series (size=100) :
    fibos = [0, 1]
    while len(fibos) < size :
        fibos.append(fibos[-1] + fibos[-2])
    return fibos


if __name__ == '__main__' :

    print fibonacci_series(size=100)
