# -*- coding: UTF-8 -*-
# 字符串操作
# str = 'Hello World'
# print str
# print str[0]
# print str[2:5]
# print str[2:]
# print str * 2
# print str + ""

'''
列表 列表用 [ ] 标识，是 python 最通用的复合数据类型
列表中值的切割也可以用到变量 [头下标:尾下标], [头下标:尾下标), 左闭右开
加号 + 是列表连接运算符，星号 * 是重复操作
'''
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
# print list
# print list[0]
# print list[1:3]
# print list[2:]
# print list[:4]
# print tinylist * 2
# print list + tinylist
# list[0] = 'helloworld'  #列表是可以修改的。

#元组 元组是另一个数据类型，类似于List
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# tinytuple = (123, 'john')
# print tuple               # 输出完整元组
# print tuple[0]            # 输出元组的第一个元素
# print tuple[1:3]          # 输出第二个至第三个的元素 
# print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2       # 输出元组两次
# print tuple + tinytuple   # 打印组合的元组
# tuple[0] = 'helloworld'   # 报错，TypeError: 'tuple' object does not support item assignment

'''
字典， 无序的对象集合。字典中元素通过对象来取
字典使用{}标识。
'''
# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
# print dict['one']          # 输出键为'one' 的值
# print dict[2]              # 输出键为 2 的值
# print tinydict             # 输出完整的字典
# print tinydict.keys()      # 输出所有键
# print tinydict.values()    # 输出所有值

#数据类型转换





