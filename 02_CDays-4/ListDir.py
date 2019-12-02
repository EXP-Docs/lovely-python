#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
print os.listdir(".")
print os.listdir("..")
print os.listdir("../..")

for root, dirs, files in os.walk("D:/commonLib/agent"):
    print root, dirs, files
    distInfo = "%s %s %s \n" % (root, dirs, files)
    open("./out/distInfo.txt", "a").write(distInfo)


