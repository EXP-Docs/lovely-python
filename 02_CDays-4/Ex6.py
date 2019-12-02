#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    读取文件 cdays-4-test.txt  内容，去除空行和注释行后，以行为单位进行排序，并将
    结果输出为 cdays-4-result.txt。
'''

import os

context = []
for line in open("./in/cdays-4-test.txt", "r").readlines():
    line = line.lstrip()
    if len(line) > 0 and not line.startswith('#'):
        context.append(line)

open("./out/cdays-4-result.txt", "w").writelines(context)