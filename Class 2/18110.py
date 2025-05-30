import sys

def custom_round(x):
    return int(x + 0.5)

N = int(sys.stdin.readline())
score = []

for _ in range(N):
    score.append(int(sys.stdin.readline()))

if N == 0 :
    print(0)

else: 
    score.sort()
    

    div = int(N * 0.15 +0.5)
    newscore = score[div: N-div]

    if len(newscore) == 0:
        print(0)
    else:
        print(custom_round(sum(newscore) / len(newscore)))
