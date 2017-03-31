import sys
#coding:utf-8

# 输出重定向
logfile = open('./log.txt', 'a')
print >> logfile, 'hhh'
logfile.close


# 程序输入
user = raw_input('Enter login name: ')
print 'your login is: ', user

# 列表用[]，元素个数和元素的值可以改变
aList = [1, 2, 3, 4]
print aList[2:4]
aList[2] = 111
print aList

# 元祖用()不可以更改，元祖可以看成是只读的列表
aTuple = ('sb', 333, 'ssss', 3.124)
print aTuple
print aTuple[1]
# aTuple[1] = 5  # TypeError: 'tuple' object does not support item assignment

# 字典
aDict = {'sb': 123, 'zhizhang': 99999}
print aDict['sb']
aDict['xxxx'] = 0
print aDict
print aDict.keys()
for key in aDict:
    print key, aDict[key]

# list comprehensions
squared = [x ** 2 for x in range(4)]
print squared

sqdEvens = [x ** 2 for x in range(10) if not x % 2]
print sqdEvens

# files
fileName = './log.txt'
fobj = open(fileName, 'r')
for eachLine in fobj:
    print eachLine,
fobj.close()