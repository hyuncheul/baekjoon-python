N = int(input())

num = [int(input()) for _ in range(N)]

num.sort()

for number in num:
    print(number)
