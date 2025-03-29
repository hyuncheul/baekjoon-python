T = int(input())
rr = []
for i in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    result = []
    for j in range(len(S)):
        result.append(S[j]*R)
    rr.append("".join(result))

for k in range(T):
    print(rr[k])