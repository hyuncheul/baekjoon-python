'''number = []

while num != '0':
    num = list(input())
    number.append(num)

for i in range(len(number)):
    for j in range(len(number[i])//2):
        if number[i][j] == number[i][len(number[i])//2-j]: 
            '''


a = ['1','2','1']
res = 0

for i in range(0,len(a)//2):
    j = len(a)-i
    if a[i] == a[j]:
        res = 1
    else: res = 0

print(res)
