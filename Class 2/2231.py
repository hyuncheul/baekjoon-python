N = int(input())
res = []
for x in range(1, N+1):
    sumres = sum(map(int, str(x)))
    if (x + sumres) == N:
        res.append(x)

if len(res) != 0:
    res.sort()
    print(res[0])

else: print(0)
