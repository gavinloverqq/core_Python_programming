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

# 变长参数
# 非关键字可变长参数（元祖）
def tupleVarArg(arg1, arg2='defualt', *theRest):
    print 'arg1 =', arg1
    print 'arg2 =', arg2
    for x in theRest:
        print 'arg rest:', x

tupleVarArg('sss', 'nnn')
tupleVarArg('sss', 'nnn', 'asa', 'dfsadgs', 'dfad')

# 关键字变量参数（字典）
def dictVarArg(arg1, arg2='defualt', **theRest):
    print 'arg1 =', arg1
    print 'arg2 =', arg2
    for x in theRest.keys():
        print 'arg rest %s : %s' % (x, theRest[x])

dictVarArg('ss', 'nnnn', d='sb', e='e')
dictVarArg('ss', 'nnnn', men=('sb1', 29))

# 混合以上两种模式
def newFoo(arg1, arg2, *nkw, **kw):
    print 'arg1 = ', arg1
    print 'arg2 = ', arg2
    for x in nkw:
        print 'non-keyword: ', x
    for k in kw.keys():
        print 'keyword arg %s: %s' % (k, kw[k])

# 注意下面的几个调用
newFoo(10, 20, 30, 40, foo=50, bar=70)
newFoo(2, 4, *(6, 8), **{'foo': 10, 'bar': 12})
aTuple = (6, 7, 8)
aDict = {'z': 9}
newFoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)


print '-' * 100
# 单元测式
def testit(func, *nkwargs, **kwargs):

    try:
        retval = func(*nkwargs, **kwargs)
        result = (True, retval)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, float, long)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        for eachVal in vals:
            retval = testit(eachFunc, eachVal)
            if(retval[0]):
                print '%s(%s) = %s' % (eachFunc.__name__, eachVal, retval[1])
            else:
                print '%s(%s) = Falid: %s' % (eachFunc.__name__, eachVal, retval[1])

test()

# lambda
a = lambda a, b=2: a + b
print a(2)
print a(2, 10)

a = lambda *z: z
print a([1, 2, 3])
print a(23, 'zxv')

# filter
from random import randint
for x in range(10):
    print randint(1, 99),

print
print '-' * 100

allNum = []
for x in range(10):
    allNum.append(randint(1, 99))

print allNum

def odd(n):
    return n % 2

print filter(odd, allNum)
print filter(lambda n: n%2, allNum)
print [n for n in allNum if n % 2]
print [n for n in [randint(1, 99) for i in range(10)] if n%2]

# map
print map((lambda x: x+2), [1, 2, 3, 4])
print map((lambda x: x**2), [1, 2, 3, 4])
print [x+2 for x in range(5)]
print [x**2 for x in range(5)]
# 多序列
print map((lambda x, y: x + y), [1, 3 ,5], [2, 4 ,6])
print map((lambda x, y: (x+y, x-y)), [2, 4, 6], [1, 3 ,5])
print map(None, [1 ,3 ,5], [2, 4, 6])


# reduce(func, [1 ,2 3]) 等价于 func(func(1, 2), 3)
print reduce((lambda x, y: x+y), range(5))

# 偏函数
from operator import add, mul
from functools import partial
add1 = partial(add, 1)
mul100 = partial(mul, 100)
print add1(10)
print mul100(10)

# 全局变量 局部变量
def foo():
    bar = 200
    print 'in foo bar is', bar
bar = 100
print 'in __main__, bar is', bar
foo()
print bar

# global 声明为全局变量
is_this_global = 'zyx'
def foo():
    global is_this_global
    is_this_local = 'abc'
    is_this_global = 'def'
    print is_this_global + is_this_local

print is_this_global
foo()
print is_this_global

# 闭包 本质上是保存一段代码执行的环境
def counter(startat=0):
    count = [startat]
    def incr():
        count[0] += 1
        return count[0]
    return incr
# 看起来和实例化counter对象并执行这个实例很相似
count = counter(10)
print count()
print count()
count2 = counter(11111)
print count2()
print count2()

# 闭包与装饰器的例子
print '*' * 100
from time import time


def logged(when):

    def log(f, *args, **kargs):
        print '''Called:
    functions: %s
    args: %r
    kargs: %r''' % (f, args, kargs)


    def pre_logged(f):

        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)

        return wrapper


    def post_logged(f):

        def wrapped(*args, **kwargs):
            now = time()
            try:
                return f(*args, **kwargs)
            finally:
                log(f, *args, **kwargs)
                print "    time delta: %s" % (time() - now)

        return wrapped

    try:
        return {'pre': pre_logged, 'post': post_logged}[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post" '


@logged("pre")
def hello(name):
    print "hello,", name


hello("world!")


# lambda作用域
x = 10
def foo():
    y = 5
    bar = lambda y=y: x +y
    print bar()
    y = 8
    print bar()

foo()

def foo():
    y = 5
    bar = lambda z: x +z
    print bar(y)
    y = 8
    print bar(y)

foo()

def foo():
    y = 5
    bar = lambda y: x +y
    print bar(y)
    y = 8
    print bar(y)

foo()

# 作用域 和 名称空间
j, k = 1, 2

def proc1():
    j, k = 3, 4
    print j, k
    k = 5

def proc2():
    j = 6
    proc1()
    print j, k

k = 7
proc1()
print j, k
j = 8
proc2()
print j, k


# 生成器
def simpleGen():
    yield 1
    yield 'xxxxxxxxxxx'

myG = simpleGen()
print myG.next()
print myG.next()
# print myG.next()  # StopIteration

for x in simpleGen():
    print x

# print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20
def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList) - 1))

for x in randGen(['ad', 'dgg', 'xxx', 1233]):
    print x


