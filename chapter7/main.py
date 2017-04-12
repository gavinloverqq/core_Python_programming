#coding=utf-8

fdict = dict((['x', 1], ['y', 2]))
print fdict

# fromkeys() 创建一个默认的字典，元素具有相同的值，如果没有给出，默认为None
ddict = {}.fromkeys(('x', 'y'), -1)
print ddict

ddict = {}.fromkeys((['x', 'y', 'z']), -1)
print ddict

edict = {}.fromkeys(('foo', 'bar'))
print edict

# traverse a dictionary
dict2 = {'name': 'earth', 'port': 80}
for keys in dict2.keys():
    print 'key = %s, value = %s' % (keys, dict2[keys])

# 可以用迭代器轻松遍历
for keys in dict2:
    print 'key = %s, value = %s' % (keys, dict2[keys])


print 'host %(name)s is running on port %(port)d' % dict2

print dict(zip(('x', 'y'), (1, 2)))
print dict([['x', 1], ['y', 2]])
print dict([('xyz'[i-1], i) for i in range(1,4)])
print dict(x=2, y=1)

# set
dict4 = {('xyz'[i-1], i) for i in range(1, 4)}
print dict4
print type(dict4)

dict2 = dict(('xyz'[i-1], i) for i in range(1, 4))
dict3 = dict(('abc'[i-1], i) for i in range(1, 4))
dict2.update(dict3)
print dict2

dict2 = {'x': 1}
dict3 = {'y': 2}
dict2.update(dict3)
print dict2

# get 方法和 [] 相似，只是查找不存在的键返回None，不用担心返回异常
dict4 = dict(a=1, b=2, c=3)
print dict4
print dict4.get('c')
print dict4.get('d')

# items() key() value() 返回值都是列表
print dict4.items()

# 重复值不会报错，但是会覆盖
print {'z': 1, 'z': 2}

# 集合只能用工厂方法set（）创建
s = set('nimashsh')
print s
s.add('sss')
print s
s.update('hello')
print s
s.remove('a')
print s
s -= set('sss')
print s

s = set((1, 2, 3))
print s
s2 = set()
s2.add(1)
s2.add(2)
s2.add(3)
print s2 == s
print s2, s

# 子集与超集
s2.add(4)
print s < s2
print set('shop') < set('cheeseshop')
print set('bookshop') >= set('shop')

# 交 并 补 异或
s1 = set('abc')
s2 = set('acdef')
print s1 | s2
print s1 & s2
print s2 - s1
print s1 ^ s2

# 不同类型的操作数，操作结果与左侧相同
s1 = frozenset('abc')
s2 = set('acdef')
print s1 | s2
print s1 & s2
print s1 ^ s2
print '*' * 100
print s2 | s1
print s2 & s1
print s2 ^ s1

# 4个仅适用于可变集合的操作符
print '*' * 100
s1 = set('abc')
s1 |= set('def')
print s1

print '*' * 100
s1 = set('abc')
s1 &= set('acedf')
print s1

print '*' * 100
s1 = set('abc')
s1 ^= set('acedf')
print s1

print '*' * 100
s1 = set('abc')
s1 -= set('acedf')
print s1

# set（）参数必须是可迭代的，即一个序列， 迭代器， 或支持迭代的一个对象， 一个文件 或 一个字典
ddict = {'a': 1, 'b': 2}
print set(ddict)

f = open('data.in', 'r')
print set(f)

# 操作符与内建函数：操作符两边必须是集合， 内建方法对象可以是可迭代的

