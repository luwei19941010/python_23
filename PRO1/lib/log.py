#-*-coding:utf-8-*-
# Author:Lu Wei

import sys,os
import logging
import time
from config import setting
from logging import handlers

#基本方法
# def get_logger():
#     logging.basicConfig(
#         filename='log1.log',
#         format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S %p',
#         level=logging.DEBUG
#     )
#     return logging

#日志处理本质
# def get_logger():
#     file_handler=logging.FileHandler('log2.log','a',encoding='utf-8')
#     fmt=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
#     file_handler.setFormatter(fmt)
#
#     logger1=logging.Logger('xxx',level=logging.ERROR)
#     logger1.addHandler(file_handler)
#     return logger1
#
# logger=get_logger()

#推荐日志处理
# def get_logger():
#     file_hander=logging.FileHandler('log3.log','a',encoding='utf-8')
#     logging.basicConfig(
#         handlers=[file_hander,],
#         format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S %p',
#         level=logging.ERROR
#     )
#     return logging
# logger=get_logger()


#推荐日志处理+分割
# def get_logger():
#     file_handler=handlers.TimedRotatingFileHandler(filename='log4.log',when='s',interval=5,encoding='utf-8')
#     logging.basicConfig(
#         handlers=[file_handler,],
#         format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S %p',
#         level=logging.ERROR
#     )
#     return logging
# logger=get_logger()


#推荐日志处理+配置文件
def get_logger():
    file_handler=handlers.TimedRotatingFileHandler(filename=setting.Log_Path,
                                                   when=setting.Log_When,
                                                   interval=setting.Log_INT,
                                                   encoding='utf-8')
    logging.basicConfig(
        handlers=[file_handler,],
        format='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p',
        level=logging.ERROR
    )
    return logging
logger=get_logger()

