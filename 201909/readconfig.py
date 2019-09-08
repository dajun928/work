#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : readconfig.py
@time : 2019/09/08 00:17:22
@func :
"""
from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')

print(cfg.sections())
print(cfg.get('debug', 'log_errors'))
print(cfg.get('server', 'nworkers'))
cfg.set('server', 'nworkers','22')
cfg.write(open('config.ini', "r+"))
print(cfg.get('server', 'nworkers'))
print(type(cfg.getint('server', 'port')))
print(cfg.get('server', 'root'))
print(type(cfg.get('server', 'port')))

a = cfg.add_section("md5")
cfg.set("md5", "value", "1234")
cfg.write(open('config.ini', "r+")) #可以把r+改成其他方式，看看结果:)


# https://www.cnblogs.com/liuyl-2017/p/7833986.html