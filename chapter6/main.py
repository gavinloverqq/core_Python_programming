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