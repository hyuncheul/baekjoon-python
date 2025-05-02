
N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
shirtnum = 0

for num in size:
    if num%T != 0:
        shirtnum += (num//T + 1)
    else:    
        shirtnum += (num//T)

print(shirtnum)

print(N//P, N%P)