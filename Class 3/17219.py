import sys
input = sys.stdin.readline

N, M = map(int, input().split())

address = {}
for _ in range(N):
    add, pd = input().split()
    address[add] = pd

for _ in range(M):
    req = input().strip()
    print(address[req])