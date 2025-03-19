c = int(input())
d = []
for i in range (c):
    a, b = map(int, input().split())
    e = a+b
    d.append(e)

for i in range (c):
    ii = str(i)
    dd = str(d[i])
    print("Case #%s: %s" % (ii, dd))








