#-*-coding:utf-8-*-
# Author:Lu Wei
import logging

file_handler=logging.FileHandler('x1.log','a',encoding='utf-8')
fmt=logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s')
file_handler.setFormatter(fmt)

logger=logging.Logger('xxxx',level=logging.ERROR)
logger.addHandler(file_handler)
logger.error('hhhhahasdhsad')