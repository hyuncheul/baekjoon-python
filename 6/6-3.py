N = int(input())

space = " "
star = "*"

for i in range(N):
    print(space * (N - i - 1) + star * (2 * i + 1))

for i in range(N - 2, -1, -1):
    print(space * (N - i - 1) + star * (2 * i + 1))