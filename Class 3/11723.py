import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    cmd = input().strip().split()
    
    if cmd[0] == 'add':
        S.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        S.discard(int(cmd[1]))
    elif cmd[0] == 'check':
        print(1 if int(cmd[1]) in S else 0)
    elif cmd[0] == 'toggle':
        x = int(cmd[1])
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S = set()
