score = []

N = int(input())

for i in range(N):
    aa = int(input())
    score.append(aa)

if N == 0:
    print(0.0)
else:
    M = max(score)
    manipulate = 0

    for i in range(N):
        manipulate += (score[i]/M)*100

    print(manipulate/N)