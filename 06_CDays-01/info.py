#!/usr/bin/python
# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParser as rcp

cfg = rcp()
cfg.add_section("Info")
cfg.set("Info", "ImagePath", "./info/image")
cfg.set("Info", "foo", "CD 信息")
cfg.write(open("./info/info.ini", "w"))

cfg.add_section("Who")
cfg.set("Who", "name", "exp")
cfg.set("Who", "phone", "12345678901")
cfg.write(open("./info/info.ini", "w"))