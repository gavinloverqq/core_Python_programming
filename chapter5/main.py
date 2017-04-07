from __future__ import division
#coding:utf-8

# 支持整形长整形
print 0xff

# 长整形能表达的数字与机器支持的虚拟内存大小有关
print 111111111111111111111111111111111111111111111111111111111111111L

print 1 << 128

# 除法 与 地板除
print 1 / 2
print 1 // 2

print 4 ** -1

num = 0XFF
print hex(num)

# coerce(a, b)  b 转换成 a 一样的数据类型
print coerce(1.2, 11111)

# divmod(a, b) 返回 商 和 余数的元祖
print divmod(10, 3)

# pow
print pow(2, 10)

# round(a, b)  对 a 四舍五入 精确到小数点后 b 位
print round(3.14444999, 5)

print int(0.5)

# print int('a')
print ord('a')
print chr(97)
# print 'a' - '0' 没有 char 类型 不能 -
