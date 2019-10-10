#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 16:41
# @Author : cqh
# @file : function_global.py
# @Software " PyCharm
x = 50

def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
