#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from thread_proxy import grepIt

def grepSearch(rootpath, keyword):
    bgn_time = time.time()
    filelist = os.listdir(rootpath)
    searchlist = []

    for file in filelist:
        filepath = "%s/%s" % (rootpath, file)
        curSThread = grepIt(filepath, keyword)
        searchlist.append(curSThread)
        curSThread.start()  # 启动线程

    for search in searchlist:
        search.join()   # 等待线程处理完成
        print "Search [", keyword, "] from [", search.filepath, "] out - ", search.reports

    print "Usage %s s" % (time.time() - bgn_time)




if __name__ == '__main__':
    grepSearch("./conf", "ke")