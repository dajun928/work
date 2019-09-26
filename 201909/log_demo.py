#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 原文链接：https://blog.csdn.net/niedongri/article/details/79304770
 多模块使用logging https://blog.csdn.net/chosen0ne/article/details/7319306
@time : 2019/09/26 23:41:59
@func :使用强大的logging模块，把输出到指定的本地pc某个路径的文件中。

一、logging的框架
1、 Loggers: 可供程序直接调用的接口，app通过调用提供的api来记录日志
2、 Handlers: 决定将日志记录分配至正确的目的地
3、 Filters:对日志信息进行过滤，提供更细粒度的日志是否输出的判断
4、 Formatters: 制定最终记录打印的格式布局

参数说明
Filename：指定路径的文件。这里使用了+—name—+是将log命名为当前py的文件名
Format：设置log的显示格式（即在文档中看到的格式）。分别是时间+当前文件名+log输出级别+输出的信息
Level：输出的log级别，优先级比设置的级别低的将不会被输出保存到log文档中
Filemode： log打开模式
    a：代表每次运行程序都继续写log。即不覆盖之前保存的log信息
    w：代表每次运行程序都重新写log。即覆盖之前保存的log信息

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
