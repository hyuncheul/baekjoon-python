N, M = map(int, input().split())

num = []
renum = []
for i in range(N):
    num.append(i+1)

for i in range(M):
    a, b = map(int, input().split())
    c = b-a+1
    renum = num[a-1:b]
    renum.reverse()
    del num[a-1:b]

    for i in range(c):
        num.insert(a-1+i, renum[i])

print(*num)