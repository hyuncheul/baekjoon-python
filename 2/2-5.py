#단계별 풀이 2-5
a, b = map(int, input().split())

ob = b-45
    
if ob < 0:
    ob = 60 + ob
    if a > 0:
        a = a-1 
    elif a <= 0:
        a = 23

print(a, ob)