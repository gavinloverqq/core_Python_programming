import string
#coding:utf-8

# sequence operator
a = [1, 2, 3]
print a[2]
print a * 3
print a[1:3]
print 1 in a

# 推荐使用extend 连接，而不是 +
b = [33, 33, 44]
print a + b
c = a.extend(b)  # 返回值 c 为 None
print c, a

a = []
for x in range(5):
    a.append(x)

# 注意负索引， 单个索引不能超边界， 切片可以超边界
print a
print a[-1]
print a[-100:100]
print a[:-1]

s = 'abcde'
i = -1
for i in range(-1, -len(s), -1):
    print s[:i]

# 输出整个s
i = None
print s[:i]

# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
a = [1, 2]
a.extend('sss')
print a

for i in [None] + range(-1, -len(s), -1):
    print s[:i]



# 步长索引
s = 'abcdefghijklmnopqrstuvwxyz'
print s[::-1]
print s[::2]

# shallow copy or deep copy?
a = [1, 2, 3]
b = a
b.extend(['sbsbsb'])
print a, b

a = [1, 2, 3]
b = list(a)
b.extend(['sbsbsb'])
print a, b

a = [1, 3, 5, 3, 33, 55, 23, 25]
print max(a)
print sorted(a, None, None, False)

# str 和 unicode 是 basestring的子类
s = '123456'
s = s[:4] + 'xxx'
print s

# 字符串不可变，删除一个字符，只能剃除不要的字符然后重组个新的字符串
s = 'hello'
print s[:2], s[4:]
s = s[:2] + s[4:]
print s

s = string.uppercase
print s

s = '%s %s' % ('dddddd', 'cccccccccc')
print s
s = s.join(('ggggggg'))
print s

# 字符串模板
from string import Template
s = Template('hello ${name} nishhi ${sb}')
print s.substitute(name='zhihang', sb='wo')

# enumerate 和 zip
s = 'foobar'
for i, v in enumerate(s):
    print i, v

a = 'foo'
b = 'bar'
print zip(a, b)


# 三引号可以包含个是字符
print '''hhhhhhhhhh
jjjj

sdfsdf'''


# unicode
ucode = u'hello'
print ucode


# list
aList = [1, 2, 3, 4, 'ssd', 3.14]
print aList
aList.remove(4)
print aList
del aList[4]
print aList

# 操作符两边使用了不同的类型
aList = [1, 2, 3]
# aList + '3'
aList.append('3')

aList = [x for x in range(10)]
print sum(aList)

# list() tuple()
aList = ['xxx', 'time', 93]
aTuple = tuple(aList)
print aList, aTuple
print aList == aTuple
annotherList = list(aTuple)
print aList == annotherList
print aList is annotherList


print aList
print aList.pop()

aTuple = (123, 345, ['dsf', 34])


# 元祖没有那么不可变
aTuple = (123, 341, ['123', 324, 'ddd'])
print aTuple[2][1]
aTuple[2][1] = ['ggg', 444]
print aTuple

# 单元素元祖需要加括号，圆括号被重载
t = ('sss')
print t
print type(t)
t = ('xxx',)
print t
print type(t)




print '*' * 100
# 深拷贝 浅拷贝
# list 默认拷贝就是浅拷贝，以下几种：完全切片操作， 利用工厂函数如list（）， 使用copy模块的copy函数
# 值改变了savings，因为savings是列表，浅拷贝的，而name是str，只能深拷贝
person = ['name', ['savings', 100.00]]
hubby = person
# hubby = person[:]
wifey = list(person)
print [id(x) for x in person, hubby, wifey]
hubby[0] = 'joe'
wifey[0] = 'jane'
print hubby, wifey
hubby[1][1] = 50.00
print hubby, wifey
print [id(x) for x in hubby]
print [id(x) for x in wifey]


print '*' * 100
# 都深拷贝 使用deepcopy函数
import copy

person = ['name', ['savings', 100.00]]
hubby = copy.deepcopy(person)
wifey = person
# wifey = copy.deepcopy(person)
print [id(x) for x in person, hubby, wifey]
hubby[0] = 'joe'
wifey[0] = 'jane'
print hubby, wifey
hubby[1][1] = 50.00
print hubby, wifey
print [id(x) for x in hubby]
print [id(x) for x in wifey]