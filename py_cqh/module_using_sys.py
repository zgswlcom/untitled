#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/10 23:44
# @Author : cqh
# @file : module_using_sys.py
# @Software " PyCharm
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')
