#-*-coding:utf-8-*-
# Author:Lu Wei
import os,sys

Base_Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_Dir)

from src.run import start

if __name__=='__main__':
    start()

