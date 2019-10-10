#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 8:16
# @Author : cqh
# @file : break.py
# @Software " PyCharm
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
