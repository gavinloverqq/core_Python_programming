#coding=utf-8

# 参数组
def add(a, b):
    return a + b

num = [2, 4]
ddict = {'a': 1, 'b': 2}
print add(*num)
print add(**ddict)

# 向前引用  函数属性
def foo():
    '''foo() doc string'''
    print 'in foo'
    bar()

def bar():
    print 'in bar'

bar.__doc__ = 'bar() doc string'
bar.version = 0.1
foo()
print bar.__doc__

# 内部函数
def foo():
    def inbar():
        print 'inbar called'
    print 'foo called'
    bar()

foo()
# inbar()

# 函数装饰器

from time import ctime, sleep
def tsfunc(func):
    def callFunc():
        print '[%s] %s()' % (ctime(), func.__name__)
        return func()
    return callFunc

@tsfunc
def foo():
    pass

for x in range(1):
    foo()
    sleep(1)

# 传递函数
def foo():
    print 'foo called'

bar = foo
bar()

def bar(argfunc):
    argfunc()

bar(foo)

# 传递和调用函数
def covertNum(func, seq):
    '''conv. sequunce of number to same type'''
    return [func(num) for num in seq]

myseq = [123, '444', 3.14, 566]
print covertNum(int, myseq)
print covertNum(float, myseq)

