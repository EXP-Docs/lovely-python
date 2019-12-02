#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    找出 0~100 的所有素数。
'''

nlist = []
for n in range(2, 100):
    nlist.append(n)
print nlist

# 筛法求素数
for curNum in range(3, 100):
    for n in nlist:
        if n >= curNum:
            break
        elif curNum % n == 0:
            nlist.remove(curNum)
            break
    curNum += 1

print nlist
