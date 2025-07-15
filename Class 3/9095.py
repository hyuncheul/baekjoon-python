import sys

num = []

T = int(sys.stdin.readline())

for _ in range(T):
    num.append(int(sys.stdin.readline()))

cs = [0]*(max(num)+1)

cs[0] = 0
cs[1] = 1
cs[2] = 2
cs[3] = 4

for i in range(4, max(num)+1):
    cs[i] = cs[i-1] + cs[i-2] + cs[i-3]

for x in num:
    print(cs[x])