#단계별풀이 2-1
a, b = map(int, input().split())

if a>b:
    print(">")
elif a<b:
    print("<")
elif a==b:
    print("==")