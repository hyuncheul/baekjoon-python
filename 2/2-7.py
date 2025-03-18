#단계별풀이 2-7
a, b, c = map(int, input().split())


if a == b == c:
    prize = 10000 + a * 1000
    print(prize)
elif a==b:
    prize = 1000+a*100
    print(prize)
elif b==c:
    prize = 1000+a*100
    print(prize)
elif a==c:
    prize = 1000+a*100
    print(prize)
elif a != b and b != c and a != c:
    if a>b:
        if a>c:
            d = a
        else: d= c
    elif b>c:
        d = b
    else: d = c
    prize = d*100
    print(prize)