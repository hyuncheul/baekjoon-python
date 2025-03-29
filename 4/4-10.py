score = []

N = int(input())

score = list(map(int, input().split()))


M = max(score)
manipulate = 0

for i in range(N):
    manipulate += (score[i]/M)*100

print(manipulate/N)