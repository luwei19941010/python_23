#-*-coding:utf-8-*-
# Author:Lu Wei
#为了避免格式问题

import logging

file_handler=logging.FileHandler('x5.log','a',encoding='utf-8')
logging.basicConfig(
    handlers=[file_handler,],
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level= logging.ERROR
)

logging.error('啊实打实大')