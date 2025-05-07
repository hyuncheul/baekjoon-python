A, B = map(int, input().split())

a_divisor = []
b_divisor = []

for i in range(1, A+1):
    if A % i == 0:
        a_divisor.append(i)

for i in range(1, B+1):
    if B % i == 0:
        b_divisor.append(i)

max_divisor = []

for j in a_divisor:
    for k in b_divisor:
        if j ==k:
            max_divisor.append(j)
max_divisor.reverse()

check = True

a = A
b = B

ax = 2
bx = 2

while check:
    if a>b :
        b = b+B
    elif a<b:
        a = a+A
    else :
        check = False

min_multiple = a

print(max_divisor[0])
print(min_multiple)

