#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
     尝试 for .. in ..循环可以对哪些数据类型进行操作?
'''

import os

for line in os.walk("D:/commonLib/agent"):
    print line

nlist = []
for n in range(1, 10):
    nlist.append(n)
print nlist