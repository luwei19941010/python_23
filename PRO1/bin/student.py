#-*-coding:utf-8-*-
# Author:Lu Wei

import os,sys

Base_Dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#a='C:\\Users\\davidlu\\PycharmProjects\\luwei-Knightsplan\\day23\\PRO1\\src'
sys.path.append(Base_Dir)
#sys.path.append(a)

from src.run import start


if __name__=='__main__':
    start()
