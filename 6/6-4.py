text = input()
N = len(text)
text = list(text)
result = []
if N%2 == 1:
    for i in range (N//2):
        if text[i] == text[(N-1)-i]:
            result.append(1)
        else: result.append(0)
elif N%2 == 0:
    for i in range(N//2):
        if text[i] == text[(N-1)-i]:
            result.append(1)
        else: result.append(0)

if result.count(1) == len(result):
    print(1)
else: print(0)