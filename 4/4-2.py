a, b = map(int, input().split())
c = list(map(int, input().split()))
d = []
count = 0
for i in range(a): 
    if b > c[i]:
        d.append(c[i])
        count += 1


for i in range(count):
    print(d[i])
