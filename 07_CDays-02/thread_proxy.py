#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
from search import search

class grepIt(Thread):
    def __init__(self, filepath, keyword):
        Thread.__init__(self)
        self.filepath = filepath
        self.keyword = keyword
        self.reports = ""

    def run(self):
         self.reports = search(open(self.filepath, "r"), self.keyword)





