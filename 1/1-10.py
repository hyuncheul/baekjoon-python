#단계별 풀이 1-10 
a = int(input())
b = int(input())


b1 = b//100
b2 = (b-b1*100)//10
b3 = (b-b1*100 - b2*10)//1

print(a*b3)
print(a*b2)
print(a*b1)
print((a*b1*100)+(a*b2*10)+(a*b3))