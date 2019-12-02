#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
     os  模块中还有哪些功能可以使用？提示：使用  dir()和 help() 。
'''

import os

help("os")

for line in os.listdir("D:/commonLib/agent"):
    print line
