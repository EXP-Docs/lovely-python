#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    利用 Python 作为科学计算器的特性，熟悉 Python 中的常用运算符，并分别求出：
        1）  12*34+78 − 132/6
        2）  （12*（34+78）− 132）/6、（86/40）**5，并利用  math 模块进行数学计算，分别求出：
            145/23 的余数
            0.5 的 sin 和 cos 值（注意 sin 和 cos 中的参数是弧度制表示法）
    提示：可通过 import math; help("math")查看 math 帮助。
'''

import math
help("math")

answer = 12 * 34 + 78 - 132 / 6
print "12 * 34 + 78 - 132 / 6 = {}".format(answer)

answer = (12 * (34 + 78) - 132) / 6
print "(12 * (34 + 78) - 132) / 6 = {}".format(answer)

answer = (86 / 40) ** 5
print "((86 / 40) ** 5 = {}".format(answer)

answer = math.fmod(145, 23)
print "math.fmod(145, 23) = {}".format(answer)

answer = 143 % 23
print "143 % 23 = {}".format(answer)

answer = math.sin(0.5)
print "math.sin(0.5) = {}".format(answer)

answer = math.cos(0.5)
print "math.cos(0.5) = {}".format(answer)

answer = math.sin(0)
print "math.sin(0) = {}".format(answer)

answer = math.cos(0)
print "math.cos(0) = {}".format(answer)
