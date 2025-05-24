N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
rangere = max(num) - min(num)
num.sort()
print(int(sum(num)/N + 0.5))

mid = N//2
print(num[mid])

pre_list = [0]*max(num)
for i in num:
    pre_list[i-1] += 1

m = max(pre_list)
idx = pre_list.index(m)
pre_list[idx] = min(pre_list)
m2 = max(pre_list)
idx2 = pre_list.index(m2)

print(pre_list[idx2])

print(rangere)
