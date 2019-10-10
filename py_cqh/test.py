#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/10/9 22:43
# @Author : cqh
# @file : test.py
# @Software " PyCharm
num = input('请输入你的工资')
num = int(num)
if num >= 30000 :
    print('有钱就是任性!')
elif num >= 20000 :
    print('哥也是月薪上万!')
elif num >= 2000 :
    print('能养活自己了!')
else :
    print('你要加油了!')
