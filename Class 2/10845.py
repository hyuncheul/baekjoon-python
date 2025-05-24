N = int(input())
main = []

for _ in range(N):
    line = input().split()
    func = line[0]
    
    if func == 'push':
        num = int(line[1])
        main.append(num)

    elif func == 'pop':
        if main:
            print(main[0])
            del main[0]
        else: print(-1)

    elif func == 'size':
        print(len(main))

    elif func == 'empty':
        if main:
            print(0)
        else: print(1)

    elif func == 'front':
        if main:
            print(main[0])
        else: print(-1)
        
    elif func == 'back':
        if main:
            print(main[-1])
        else: print(-1)