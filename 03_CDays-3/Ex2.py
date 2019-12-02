#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    读取某一简单索引文件 cdays-3-test.txt，其每行格式为：文档序号 关键词，现须根据
    这些信息将它转化为倒排索引，即统计关键词在哪些文档中，格式如下：包含该关
    键词的文档数  关键词  =>  文档序号。其中，原索引文件作为命令行参数传入主程序，
    并设计一个 collect 函式统计“关键字↔序号”结果对，最后在主程序中输出结果至
    屏幕。
'''

def collect(idx_file, key):
    dict = {}
    for line in open(idx_file, 'r').readlines():
        args = line.split(' ')
        if len(args) == 2:
            dict[args[0]] = args[1].rstrip()

    appear = 0
    results = []
    for k in dict.keys():
        v = dict.get(k)
        if v.__contains__(key):
            appear += 1
            results.append('=>'.join([v, k]))

    print appear
    for result in results:
        print result
    print '---------------------------------------------'


collect("./in/cdays-3-test.txt", 'key2')
collect("./in/cdays-3-test.txt", 'key1')
collect("./in/cdays-3-test.txt", 'exp')
collect("./in/cdays-3-test.txt", 'ke')


