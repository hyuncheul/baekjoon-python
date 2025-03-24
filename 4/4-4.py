a = []
for i in range(9):
    a.append(int(input()))

b = sorted(a)


c = b[8]
d = int(a.index(c))

print(c)
print(d+1)