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


cdWalker("D:/commonLib/agent", './out/cd_info.txt')
