### day23

#### 今日内容

- 单例模块

```
class Foo:
	pass
obj1=Foo()#实例，对象
obj2=Foo()#实例，对象
```



- 日志模块（logging）
- 程序的目录结构

内容回顾&作业

#### 1.补充

- 字符串格式化

```

# msg='我是%s,年龄%s'%('陆威','19')
# print(msg)

# msg='我是%(n1)s,年龄%(n2)s'%{'n1':'陆威','n2':'19'}
# print(msg)

msg='我是{0},年龄{1}'.format('陆威','19')
print(msg)

msg='我是{name},年龄{age}'.format(name='陆威',age='19')
print(msg)
```

- 字典

```
#py3.7之后才是有序的，但是可以使用 OrderedDict

from collections import OrderedDict

info = OrderedDict()
info['k1']=123 #__setitem__
info['a']      #__getitem__
info['k2']=456 
print(info)
```



```
class Foo(object):
	def get(self):
		pass
obj=Foo()
#if hasattr(obj,'get')
	getattr(obj,'get')
v1=getattr(obj,'get',None)#推荐
###v1 None
```

### 内容详细

23种设计模式。

#### 1.单例模式

​	无论实例化多少次，永远用的都是第一次实例化出的对象。

```
calss Foo(object):
	pass
#多例，每个实例化一次就创建一个新的对象
obj1=Foo()#实例，对象
obj2=Foo()#实例，对象
#单例，无论实例化多少次，都用第一次创建的那个对象。
```

单例模式标准

```
class Singleton(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            return cls.instance==object.__new__(cls)
        return cls.instance
obj1=Singleton()
obj2=Singleton()
print(obj1,obj2)
#不是最终，加锁必须。
```

合适使用单例模式

```
多个客户端连接数据库时
```

```
class FileHelper(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance= object.__new__(cls)
        return cls.instance
    def __init__(self,path):
        self.file_object=open(path,mode='r',encoding='utf-8')

ob1=FileHelper('x')
print(ob1.file_object.read(1))
ob2=FileHelper('x')
print(ob2)
```

#### 2.模块

多次导入重新加载

```
import jd #第一次加载:会加载一边jd中所有的内容
import jd #第一次直接或者间接加载过了，之后都不会再次加载

print(123)

```

```
import importlib
import jd
importlib.reload(jd)#主动再次加载 
print(123)
```

通过模块导入的特性，也可以实现单例模式。

```
#jd.py
class Foo(object):
	pass
obj=Foo()
```

```
#app.py
import jd #加载jd.py，最后会实例化一个Foo对象并赋值给obj
print(jd.obj)
```

#### 3.日志（模块）

- 基本应用（存在编码的错误）
- 日志处理本质（3个对象，logger/FileHander/Formatter
- 推荐处理日志方式
- 推荐日志处理+日志分割

注意事项：

```
#在应用日志时，如果想要保留异常的堆栈信息
 logging.error(msg,exc_info=True)#exc_info=True显示详细报错
```



```
import logging

logging.basicConfig(
    filename='cmdb1.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG
)

#logging日志，第二次无效
logging.basicConfig(
    filename='cmdb2.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG
)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
logging.log(10,'log')
```

logging模块应用

```
import logging
import requests

logging.basicConfig(
    filename='cmdb.log',
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=logging.DEBUG
)
try:
    requests.get('http://www.xx.com')
except Exception as e:
    msg=str(e)
    logging.error(msg,exc_info=True)#exc_info=True显示详细报错
```

日志格式化

![image-20200117134451615](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200117134451615.png)

日志处理本质

```
import logging

file_handler=logging.FileHandler('x1.log','a',encoding='utf-8')
fmt=logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s')
file_handler.setFormatter(fmt)

logger=logging.Logger('xxxx',level=logging.ERROR)
logger.addHandler(file_handler)
logger.error('hhhhahasdhsad')
```

推荐日志处理

```
import logging
file_handler=logging.FileHandler('x5.log','a',encoding='utf-8')
logging.basicConfig(
    handlers=[file_handler,],
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level= logging.ERROR
)

logging.error('啊实打实大')
```

日志切割+推荐日志处理

```python
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
```

#### 4.项目结构目录

- 脚本

![image-20200117153419425](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200117153419425.png)

- 单可执行文件

![image-20200117155455107](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200117155455107.png)

- 多可执行文件

![image-20200117160100630](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200117160100630.png)





