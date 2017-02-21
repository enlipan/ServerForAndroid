# coding=utf-8

"""
元类：
1.拦截类的创建
2.修改类
3.返回经过修改之后的类


type 定义创建类的类，也是一个类，类似 'str','int'

"""

class UpperAttrMetaClass(type):
    """
    __new__ 函数的改写，该函数在init之前被调用，该函数是用于创建对象并返回对象的，
    而init则用于初始化创建的对象，__new__函数用于控制对象的创建，这里改写创建对象的类（对象）的创建

    __init__ 改写
    __call__ 函数--（http://www.artima.com/weblogs/viewpost.jsp?thread=240845）

    """
    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(),value) for name,value in attrs)
        return type(future_class_name,future_class_parents,uppercase_attr)

class UpperAttrMetaClassOOP(type):

    def __new__(upperattr_metaclass, future_class_name, future_class_parents, future_class_attr):
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(),value) for name,value in attrs)
        return type.__new__(future_class_name,future_class_parents,uppercase_attr)