#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
    1.编程实现以下功能，并进行最大化的优化：遍历指定目录下的所有文件，找出其中
      占用空间最大的前 3 个文件。

    2.利用 ConfigParser，将上述题目中产生的结果按照 cdays+1-my.ini  格式存储到文件
      cdays+1-result.txt 中。
'''

import os
from ConfigParser import RawConfigParser as rcp

def replace(iAry, num):
    min = iAry[0]
    min_idx = -1
    idx = 0
    for n in iAry:
        if min >= n:
            min = n
            min_idx = idx
        idx += 1

    if min_idx >= 0 and num > iAry[min_idx]:
        iAry[min_idx] = num
    else:
        min_idx = -1
    return min_idx



def find(dir_path):
    paths = [''] * 3
    sizes = [0] * 3
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            path = '\\'.join([root, file])
            size = os.stat(path).st_size
            idx = replace(sizes, size)
            if idx >= 0:
                paths[idx] = path

    result = [[paths[0], sizes[0]],
              [paths[1], sizes[1]],
              [paths[2], sizes[2]]]
    return result



cfg = rcp()
cfg.add_section("Path & Size")
for path, size in find('C:\DRIVERS'):
    cfg.set("Path & Size", path, size)
cfg.write(open("./info/find_info.ini", "w"))

