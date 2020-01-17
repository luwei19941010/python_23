#-*-coding:utf-8-*-
# Author:Lu Wei
import logging
import time
from logging import handlers
# file_handler=logging.FileHandler('x5.log','a',encoding='utf-8')
file_handler= handlers.TimedRotatingFileHandler(filename='time.log',when='s',interval=5,encoding='utf-8')
logging.basicConfig(
    handlers=[file_handler,],
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level= logging.ERROR
)

for i in range(1,1000):
    time.sleep(1)
    logging.error(str(i))