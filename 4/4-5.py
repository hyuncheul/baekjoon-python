N, M = map(int, input().split())

main = []
a = []
b = []
c = []

for i in range(N):
    main.append(0)

for i in range(M):
    aa, bb, cc = map(int, input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)


for i in range(M):
    aaa = a[i]
    while aaa <= b[i]:
        main[aaa - 1] = c[i]
        aaa += 1

for i in range(N):
    print(main[i])