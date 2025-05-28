import sys
N, K = map(int, sys.stdin.readline().split())
coin = []
for i in range(N):
    coin.append(int(input()))
    
coin.reverse()
cnt = 0
money = K
j = 0
while money > 0:
    if coin[j] <= money:
        money = money - coin[j]
        cnt += 1
    elif coin[j] > money:
        j += 1

print(cnt)