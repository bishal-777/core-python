s = {10, 20, 30}
print(s)
print(type(s))
s1 = set()
print(type(s1))

s.add(10)
print(s)
s.add(40)
print(s)
s.add(50)
print(s)
s.remove(40)
print(s)

print(50*"-")

fs = frozenset(s)
print(type(fs))