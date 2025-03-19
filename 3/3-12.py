import sys

a = sys.stdin.read().split()

for i in range(0, len(a), 2):
    aa = int (a[i])
    bb = int (a[i+1])
    print(aa+bb)
    