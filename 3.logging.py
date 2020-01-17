#-*-coding:utf-8-*-
# Author:Lu Wei
import logging
import requests

logging.basicConfig(
    filename='cmdb.log',#中文出现乱码因为cmdb.log编码问题
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.ERROR
    # level= 30
)
try:
    requests.get('http://www.xxx.com')
except Exception as e:
    msg=str(e)
    logging.error(msg,exc_info=True)
    # logging.log(50,msg)
