N = int(input())
numbers = list(map(int, input().split()))
prime = []

for num in numbers:

    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        prime.append(num)
    
print(len(prime))