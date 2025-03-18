#단계별 풀이 2-6
a, b = map(int, input().split())
c = int(input())
c1 = c//60
c2 = c%60


if b+c2 >= 60:
    if(a+c1 >= 23):
        a = a+c1 - 23
        b = b+c2 - 60
        print(a, b)
    else: 
        a = a+c1
        b = b+c2 - 60
        print(a, b)

else:
    if(a+c1 >= 23):
        a = a+c1 - 23
        b = b+c2
        print(a, b)
    else: 
        a = a+c1
        b = b+c2
        print(a,b)