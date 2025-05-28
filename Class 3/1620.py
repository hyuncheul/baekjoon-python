import sys
N, M = map(int, sys.stdin.readline().split())
K = N + M
cnt = []

people = []
for i in range(K):
    people.append(input())

for peo in people:
    a = people.count(peo)
    if a >= 2 and peo not in cnt:
        cnt.append(peo)

print(len(cnt))

for pr in cnt:
    print(pr)