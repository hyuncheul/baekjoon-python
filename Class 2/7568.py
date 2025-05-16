N = int(input())
box = []

for i in range(N):
    x, y = map(int, input().split())
    if i == 0 :
        box.append([x,y])
    else:
        j = 0
        if box[j][0] > x and box[j][1] > y:
            box.insert(j-1, [x,y])
        elif box[j][0] < x and box[j][1] < y:
            j += 1
        else: box.



print(box)

