door = []
def check(x):
    for a in x:
        if a in '()[]':
            door.append(a)
    return

sentence = []
i = 0

while(True):
    sen = input().split()
    sentence.append(sen)
    if sen == '.':
        break

for i in range(len(sentence)):
    check(sentence[i])


