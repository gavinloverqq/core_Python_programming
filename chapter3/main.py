# continuation
print "sssss" \
      "dddddd"

# Multiple Statements on a Single Line
print 'a'; print 'b'

# Multiple Assignment
x1 = y1 = z1 = 1

# "Multuple" Assignment
(x, y, z) = (111, "xxx", 3.14)
print x, y, z

def test():
    "test doc"
    print 'test work'

print test.__doc__

if __name__ == '__main__':
    test()

x = 3.14
y = x
x = 4
print y