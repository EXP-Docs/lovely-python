#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
     格式化声明，还有哪些格式可以进行约定?
'''

import math

print "%s %s" % ('Hello', 'World')
print "{} {}".format('Hello', 'World')
print "{0} {1}".format('Hello', 'World')
print "{1} {0}".format('World', 'Hello')
print "{arg2} {arg1}".format(arg1='World', arg2='Hello')
print "pi = %5.3f" % math.pi
print "e = %i" % math.e