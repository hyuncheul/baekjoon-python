import sys

N, M = map(int, sys.stdin.readline().split())

heard = set()
for _ in range(N):
    heard.add(input().strip())

seen = set()
for _ in range(M):
    seen.add(input().strip())

result = sorted(heard & seen)

print(len(result))
for name in result:
    print(name)