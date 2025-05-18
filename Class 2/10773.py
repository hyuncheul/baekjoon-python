K = int(input())

num = []
for i in range(K):

    n = int(input())
    if n != 0 :
        num.append(n)
    else:
        num.pop()

print(sum(num))
