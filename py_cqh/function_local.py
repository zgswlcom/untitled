#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 16:36
# @Author : cqh
# @file : function_local.py
# @Software " PyCharm
x = 50


def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)
