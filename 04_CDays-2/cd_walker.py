#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

print sys.argv

def cdWalker(cdrom, to_file):
    export = []
    for root, dirs, files in os.walk(cdrom):
        export.append("%s %s %s\n" % (root, dirs, files))
    open(to_file, "w").writelines(export)


'''
    检索指定目录下所有文件中包含关键字的行（不包括子目录）
'''
def cdGrep(cdPath, keyWord):
    filelist = os.listdir(cdPath)   # 列出目录下所有文件
    print filelist

    for filename in filelist:
        if ".txt" in filename:      # 文件过滤
            file = open("/".join([cdPath, filename]), "r") # 打开文件
            for line in file.readlines():      # 读取文件每一行
                if keyWord in line: # 检查关键字是否在行中
                    print " -> ".join([filename, line.rstrip()])



