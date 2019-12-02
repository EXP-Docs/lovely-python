#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    1.      自动判定你自个儿或是朋友的 Blog  是什么编码的？
    2.      如果是非 utf-8  的，请编写小程序自动将指定文章转换成 utf-8  编码保存。
'''


def smartcode(str):
    charsets = ['ISO-8859-1', 'UTF8', 'GBK', 'UNICODE']
    enCharset = None
    for charset in charsets:
        try:
            cstr = unicode(str, charset).encode('utf8')
            enCharset = charset
            print "[{}] SUCCESS {} TO UTF8: \n{}".format(str, charset, cstr)
            break
        except:
            print "[{}] ERROR {} TO UTF8".format(str, charset)
    return enCharset



print smartcode('中文')
print smartcode('中English')
print smartcode('English')



