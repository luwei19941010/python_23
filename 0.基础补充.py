#-*-coding:utf-8-*-
# Author:Lu Wei


# msg='我是%s,年龄%s'%('陆威','19')
# print(msg)

# msg='我是%(n1)s,年龄%(n2)s'%{'n1':'陆威','n2':'19'}
# print(msg)

# msg='我是{0},年龄{1}'.format('陆威','19')
# print(msg)

# msg='我是{name},年龄{age}'.format(name='陆威',age='19')
# print(msg)

from collections import OrderedDict

info = OrderedDict()
info['k1']=123
info['k2']=456
print(info)