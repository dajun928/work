#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : ccccc.py
@time : 2019/09/26 23:41:59
@func : 
"""
import logging

filename = './log/' + __name__ + '.log'
# format = '[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]'
format = '%(asctime)s - %(levelname)s - Model:%(filename)s - Fun:%(funcName)s - Message:%(message)s - Line:%(lineno)d'
level = logging.DEBUG
filemode = 'a'
datefmt = '%Y-%m-%d%I:%M:%S %p'
logging.basicConfig(filename=filename, format=format, level=level, filemode=filemode, datefmt=datefmt)

logging.error("这是一条error信息的打印")
logging.info("这是一条info信息的打印")
logging.warning("这是一条warn信息的打印")
logging.debug("这是一条debug信息的打印")
