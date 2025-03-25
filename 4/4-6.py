N, M = map(int, input().split())

num = []
for i in range(N):
    num.append(i+1)

for i in range(M):
    a, b = map(int, input().split())
    na = num[a-1] 
    nb = num[b-1]
    num[a-1] = nb
    num[b-1] = na

print(*num)