N, M = map(int, input().split())

card = list(map(int, input().split()))
card.sort()
result = []
res = 0

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(i+2, len(card)):
            res = card[i]+ card[j] + card[k]
            if res <= M: 
                result.append(res)

result.sort()
result.reverse()
print(result[0])
