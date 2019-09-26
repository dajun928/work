#!/usr/bin/python
# -*- coding: utf-8 -*-  
"""
@version : 
@file : mod.py
@time : 2019/09/27 00:25:50
@func : 
"""
import logging
import submod

logger = logging.getLogger('main.mod')
logger.info('logger of mod say something...')


def testLogger():
    logger.debug('this is mod.testLogger...')
    submod.tst()

