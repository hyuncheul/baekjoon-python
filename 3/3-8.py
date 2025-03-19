c = int(input())
aa = []
bb = []
d = []
for i in range (c):
    a, b = map(int, input().split())
    e = a+b
    aa.append(a)
    bb.append(b)
    d.append(e)

for i in range (c):
    ii = str(i+1)
    dd = str(d[i])
    print("Case #%s: %d + %d = %d" % (ii, aa[i], bb[i], d[i]))
