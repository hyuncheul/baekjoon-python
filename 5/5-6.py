text = input()
abc = []
alpha = [chr(i) for i in range(97, 123)]
i = 0
for alphabet in alpha:
    abc.append(text.find(alphabet))
    i +=1

print(*abc)