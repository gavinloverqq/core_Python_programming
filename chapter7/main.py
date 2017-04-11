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



