CODEC = 'utf-8'
FILE = 'unicode.txt'

out = u'weocaoosodfjskfnajs'
byte_out = out.encode(CODEC)

f = open(FILE, 'w')
f.write(byte_out)
f.close()

f = open(FILE, 'r')
byte_in = f.read()
f.close()

fin = byte_in.decode(CODEC)
print fin

