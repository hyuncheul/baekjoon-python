N = int(input())
dot = []

for _ in range(N):
    x, y = map(int, input().split())
    dot.append([x,y])

dot.sort(key = lambda x : (x[0], x[1]))

for i in range(N):
    print(dot[i][0],dot[i][1])