N = int(input())

string = []
for i in range(N):
    str = input()
    string.append(str)

set_string = list(set(string))

set_string.sort(key=lambda x: (len(x), x))

for s in set_string:
    print(s)
