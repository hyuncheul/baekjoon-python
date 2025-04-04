text = input()
text = text.upper()
text = list(text)
alphabet = ['A','B','C','D','E','F','G',
            'H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U',
            'V','W','X','Y','Z']

count = []

for i in alphabet:
    count.append(text.count(i))

if count.count(max(count)) > 1 :
    print('?')
else:
    max_index = count.index(max(count))
    print(alphabet[max_index])