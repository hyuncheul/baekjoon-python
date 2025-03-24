a = int(input())
c = list(map(int, input().split()))

c.sort()

print(c[0], c[a-1])