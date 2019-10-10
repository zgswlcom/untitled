#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 16:19
# @Author : cqh
# @file : continue.py
# @Software " PyCharm
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length') # 自此处起继续进行其它任何处理
