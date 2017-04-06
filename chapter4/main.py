#coding:utf-8
# slice
slc = []
for x in range(10):
    slc.append(x)
print slc[1:3][7:9]  # 多维切片如何使用
print slc[1:9:3]  # [start:end:step]
print slc[::3]
print slc[::-1]

# 支持多个对象一起比较
x, y, z = 1, 2, 3
print x < y < z

# 值传递？引用传递？ id 类似取地址
a = 1
print id(a)
b = 2
print id(b)
c = a
print id(c)
d = 1
print id(d)
print a is c, d is a, b is not a

# 可变对象 类似引用传递
print '*' * 100
def changeA(a):
    for x in range(10):
        a.append(x)
a = [x for x in range(3)]
print a
changeA(a)
print a

# 不可变对象 number string tuple 类似值传递
print '*' * 100
def changeB(b):
    b = (1, 2, 3)
b = (5, 5, 5)
print b
changeB(b)
print b

# Standard Type Built-in Functions
a, b = 4, 15
print cmp(a, b), cmp(b, a), cmp(1, 1)  # i < 0 if a < b print -1
a, b = 'abc', 'xyz'
print cmp(a, b), cmp(b, a), cmp(1, 1)

# str() repr() 和 ``
print str(2e10)  # str可用于字符串输出，无法与用eval求值
print repr([2, 'xxxx', 3]) # 反之


# eval 是个很神奇的东西
g = {'a': 1, 'b': 2}
print eval('a+111', g)
# print g  有惊喜

def displayType(num):
    print num, 'is',
    if isinstance(num, (int, long, float)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all'

displayType(111)
displayType(1.111)

import types
print type(3) == types.IntType

