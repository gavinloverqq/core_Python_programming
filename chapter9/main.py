#coding=utf-8

f = open('data.in', 'r')
for x in f:
    print x  # 输出了换行符
f.close()

f = open('data.in', 'w+')
print f.tell()
f.write('hhhhhhhhhhhhhhhhhhhh\n')
print f.tell()
f.seek(0, 0)
print f.readline()
print f.tell()
f.close()

import pickle
obj = {'a': 1, 'b': 2}
pickle.dump(obj, open('tmp.txt', 'w'))
obj2 = pickle.load(open('tmp.txt', 'r'))
print obj2

