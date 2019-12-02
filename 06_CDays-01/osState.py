#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print os.stat("./info")
print os.stat("./info").st_size

print os.stat("./info/info.ini")
print os.stat("./info/info.ini").st_size