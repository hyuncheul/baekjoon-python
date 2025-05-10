T = int(input())
a=[]
b=[]

for i in range(T):
    k = int(input())
    n = int(input())
    a.append(k)
    b.append(n)


for t in range(T):
    people = []
    for i in range(a[t]+1):
        floor = []
        for j in range(1, b[t]+1):
            if i == 0:
               floor.append(j)
            elif j == 1:
                floor.append(1)
            else: floor.append(floor[j-2]+people[i-1][j-1])
        people.append(floor)
    print(people[a[t]][b[t]-1])

