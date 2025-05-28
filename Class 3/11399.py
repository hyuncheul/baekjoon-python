import sys
N = int(input())
P = list(map(int, sys.stdin.readline().split()))

wait = 0
tot = 0
before = 0
P.sort()

for atm in P:
    before = tot
    tot = before + wait + atm
    wait += atm

print(tot)
