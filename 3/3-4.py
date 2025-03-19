total = int(input())
num = int(input())

calcul = 0

for i in range (num):
    a, b = map(int, input().split())
    e = a*b
    calcul = calcul + e

if calcul == total:
    print("Yes")

else: print("No")
