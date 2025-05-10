A, B, V = map(int, input().split())

day = 0


if V % (A-B) == 0 :
    day = V // (A-B) - 1 
else: day = V // (A-B) + 1



print(day)