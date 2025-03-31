test = [1, 1, 2, 2, 2, 8]
study = list(map(int, input().split()))
result = []
for i in range(6):
    result.append(test[i] - study[i])

print(*result)