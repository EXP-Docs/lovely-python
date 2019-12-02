#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def smartcode(str):
    try:
        str = unicode(str, 'gbk').encode('utf8')
    except:
        print '[{}] ERROR FROM GBK TO UTF8'.format(str)
    return str

def format_cd_info(root, dirs, files):
    export = "\n" + smartcode(root) + ":\n"
    for d in dirs:
        export += "\t-d " + smartcode(d) + "\n"
    for f in files:
        export += "\t-f %s\n" % (smartcode(f))
    return export



for root, dirs, files in os.walk(".\\in"):
    print format_cd_info(root, dirs, files)


