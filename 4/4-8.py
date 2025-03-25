num = []

for i in range(10):
    innum = int(input())
    num.append(innum % 42)

print(len(set(num)))