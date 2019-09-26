#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : https://blog.csdn.net/chosen0ne/article/details/7319306
@file : main.py
@time : 2019/09/27 00:25:28
@func : 
"""
import logging
import logging.config

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')

logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'mod\'...')
import mod

logger.debug('let\'s test mod.testLogger()')
mod.testLogger()
root_logger.info('finish test...')

