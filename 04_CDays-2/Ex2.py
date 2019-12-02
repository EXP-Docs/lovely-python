#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
    编写一个类，实现简单的栈。数据的操作按照先进后出（FILO）的顺序。主要成员
    函式为 put(item)，实现数据 item 插入栈中；get()，实现从栈中取一个数据。
'''

class stack():
    def __init__(self):
        self.STACK = []

    def put(self, item):
        self.STACK.append(item)

    def get(self):
        idx = len(self.STACK) - 1
        item = None
        if idx >= 0:
            item = self.STACK.pop(idx)
            return item

    def list_all(self):
        return self.STACK


st = stack()
st.put('aaa')
st.put('bbb')
st.put('ccc')
st.put('bbb')
print st.list_all()
print st.get()
print st.list_all()


