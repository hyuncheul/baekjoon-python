N = int(input())
spot = []
for i in range(N):
    x, y = map(int, input().split())
    spot.append([x,y])

spot.sort(key = lambda x: (x[1],x[0]))

for i in range(N):
    print(spot[i][0],spot[i][1])