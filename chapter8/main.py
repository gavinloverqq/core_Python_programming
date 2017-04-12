#coding=utf-8

# if else
a, b, c = 1, 3, 2
if not a and b == 3 or c != 2:
    print "True"
else:
    print 'false'

# 悬挂else
a, b, c = 1, 2, 3
if a > 1:
    if b == 1:
        print 'b'
else:
    print 'a'

# elif
if a > 1:
    print a
elif b == 2:
    print b
elif c > 2:
    print c

# 条件表达式 X if C else Y
a, b = 3, 4
x = b if a < b else a
print x

# while
count = 1
while(count < 9):
    print 'xxx'
    count += 1

aList = [x for x in range(30) if x % 2 == 0]
for a in aList:
    print a,
print
print '*' * 100
for b in range(len(aList)):
    print aList[b],
print
print '*' * 100
for i, it in enumerate(aList):
    print "%d: %d" % (i, it)


# xrang() 和 range（）类似 但是效率更高，不生成真个列表

for b in xrange(len(aList)):
    print aList[b],
print
print '*' * 100

# 与序列相关的内建函数
aList = [2, 54, 11, 33]
for x in sorted(aList):
    print x,
print
for x in reversed(aList):
    print x,
print

# while else 与 for else
a, b = 4, 5
while a > 1:
    print 'xx',
    a -= 1
else:
    print 'mmm'

# 迭代器
aTuple = (123, 'sss', 3.12)
i = iter(aTuple)
print i
print i.next()


# 列表解析
print map(lambda x: x**2, range(6))
print [x ** 2 for x in range(6)]
aList = [x for x in range(30)]
print filter(lambda x: x % 2, aList)
print [x for x in aList if x % 2]

# 计算单词个数
f = open('text.data', 'r')
print len([word for line in f for word in line.split()])

import os
print os.stat('text.data').st_size

f.seek(0)
print sum([len(word) for line in f for word in line.split()])

f.seek(0)
print sum(len(word) for line in f for word in line.split())
f.close()

print max(len(s.strip()) for s in open('text.data', 'r'))



