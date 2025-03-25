student = []

for i in range(30):
    student.append(i+1)

for i in range(28):
    a = int(input())
    student.remove(a)

for i in range(2):
    print(student[i])