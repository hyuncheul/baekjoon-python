N = int(input())
a = []
for _ in range(N):
    A = int(input())
    a.append(A)

a.sort()

for i in range(N):
    print(a[i])