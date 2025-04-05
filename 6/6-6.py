text = input()
copy = text
Croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for char in Croatia:
    copy = copy.replace(char,'a')


print(len(copy))