#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import cmd
from cd_walker import *

''' 默认库不存在 cmd.Cmd ，可能需要导入第三方包（或者python版本问题） -- by exp

class PyCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)                # initialize the base class

    def help_EOF(self):
        print " 退出程序  Quits the program"

    def do_EOF(self, line):
        sys.exit()

    def help_walk(self):
        print " 扫描光盘内容  walk cd and export into *.cdc"

    def do_walk(self, filename):
        if filename == "":filename = raw_input(" 输入 cdc 文件名 :: ")
        print " 扫描光盘内容保存到 :'%s'" % filename

    def help_dir(self):
        print " 指定保存 / 搜索目录 "

    def do_dir(self, pathname):
        if pathname == "": pathname = raw_input(" 输入指定保存 / 搜索目录 : ")

    def help_find(self):
        print " 搜索关键词 "

    def do_find(self, keyword):
        if keyword == "": keyword = raw_input(" 输入搜索关键字 : ")
        print " 搜索关键词 :'%s'" % keyword
'''

if __name__ == '__main__':      # this way the module can be
    # cdc = PyCDC()            # imported by other programs as well
    # cdc.cmdloop()
    cdWalker("D:/commonLib/agent", './out/cd_info.txt')
    cdGrep("./in", "key")