#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 16:58
# @Author : cqh
# @file : function_return.py
# @Software " PyCharm
def maximum(x, y):
    if x > y:
        return x
    elif x == y: 
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))
