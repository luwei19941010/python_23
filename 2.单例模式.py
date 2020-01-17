#-*-coding:utf-8-*-
# Author:Lu Wei


class Singleton(object):
    instance=None
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance= object.__new__(cls)
        return cls.instance
obj1=Singleton()
obj2=Singleton()
print(obj1,obj2)

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

