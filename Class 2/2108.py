N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
rangere = max(num) - min(num)
num.sort()
if sum(num)/N >= 0:
    print(int(sum(num)/N + 0.5))
else:
    print(int(sum(num)/N - 0.5))

mid = N//2
print(num[mid])

pre_list = [0] * 8001
for i in num:
    pre_list[i + 4000] += 1

m = max(pre_list)
mode_list = []
for i in range(8001):
    if pre_list[i] == m:
        mode_list.append(i - 4000)

if len(mode_list) == 1:
    print(mode_list[0])
else:
    print(mode_list[1])


print(rangere)
