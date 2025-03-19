#단계별 풀이 2-6
a, b = map(int, input().split())
c = int(input())
c1 = c//60
c2 = c%60

b= b+c2
if b >= 60:
    a = a+1
    b = b-60

a = a+c1
if a>=24:
    a= a-24
print(a,b)