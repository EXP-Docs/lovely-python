#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    在前文的 grep 实现例子中，没有考虑子目录的处理方式，因为如果直接 open 目录进行读
    操作，会出现错误，所以请读者修改这个示例代码，以便考虑到子目录这种特殊情
    况，然后把最后探索出的 cdcGrep()嵌入  pycdc-v0.5.py  中，实现完成版本的
    PyCDC。
    提示：子目录处理，可以先判断，如果是子目录，就可以递归调用 cdcGrep()函式。
'''

import os

'''
    检索指定目录下所有文件中包含关键字的行（包括子目录）
'''
def cdGrep(cdPath, keyWord, step):
    list = os.walk(cdPath)   # 列出目录下所有文件

    for root, dirs, files in list:
        for filename in files:
            if ".txt" in filename:      # 文件过滤
                file = open("/".join([root, filename]), "r") # 打开文件
                for line in file.readlines():      # 读取文件每一行
                    if keyWord in line: # 检查关键字是否在行中
                        print " -> ".join([filename, line.rstrip()])


cdGrep("./in", "key", 1)