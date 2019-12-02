#!/usr/bin/python
# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParser as rcp

def search(file, keyword):
    report = "line: "
    upKeyword = keyword.upper()

    lineCnt = 1
    for line in file.readlines():
        if upKeyword in line.upper():
            report += "%i, " % lineCnt
        lineCnt += 1
    return report