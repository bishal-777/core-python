b = [10, 20, 30, 40]    #can take values ranging 0-256
by =bytes(b)
print(type(by))
print(by[0:3])

for i in by:
    print(i)

by = bytearray(b)
print(type(by))

by[0] = 255
for i in by:
    print(i)