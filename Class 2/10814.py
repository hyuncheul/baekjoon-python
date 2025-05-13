N = int(input())

people = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append((age, i, name)) 

people.sort(key=lambda x: (x[0], x[1]))

for age, _, name in people:
    print(f"{age} {name}")