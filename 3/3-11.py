count = 0
result = []

while(1):
    a, b = map(int, input().split())
    if a==0 and b==0:
        for i in range(count):
            print(result[i])
        
        break
    else: 
        num = a+b
        result.append(num)
        count += 1
