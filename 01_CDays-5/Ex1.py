#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    计算今年是否是闰年。
    判断闰年条件，满足年份模 400 为 0，或者模 4 为 0 但模 100不为 0。
'''

import sys

print "请输入年份:"
year = sys.stdin.readline()
year = int(year)

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print "{} 年是闰年".format(year)
else:
    print "{} 年不是闰年".format(year)
