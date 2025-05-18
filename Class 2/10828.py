N = int(input())

for _ in range(N):
    linesplit = []
    line = input()
    linesplit = line.split()
    func = linesplit[0]
    num = int(linesplit[1])
    
    if func == 'push':
        print(num)