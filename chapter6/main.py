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