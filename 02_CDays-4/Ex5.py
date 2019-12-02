#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    下面的写入文件模式好吗?  有改进的余地吗?
    下面是 CDay − 4-5.py  ，它好在哪里?
        1 # -*- coding: utf-8 -*-
        2 import os
        3 export = ""
        4 for root, dirs, files in os.walk('/media/cdrom0'):
        5   export+="\n %s;%s;%s" % (root,dirs,files)
        6 open('mycd2.cdc', 'w').write(export)
    以下的 CDay − 4-6.py 又更加好在哪里?
        1 # -*- coding: utf-8 -*-
        2 import os
        3 export = []
        4 for root, dirs, files in os.walk('/media/cdrom0'):
        5     export.append("\n %s;%s;%s" % (root,dirs,files))
        6 open('mycd2.cdc', 'w').write(''.join(export))
'''

import os

export = ""
for root, dirs, files in os.walk('D:/commonLib/agent'):
    export += "\n %s;%s;%s" % (root, dirs, files)
open('./out/ex5-1-mycd2.txt', 'w').write(export)


export = []
for root, dirs, files in os.walk('D:/commonLib/agent'):
    export.append("\n %s;%s;%s" % (root, dirs, files))
open('./out/ex5-2-mycd2.txt', 'w').write(''.join(export))