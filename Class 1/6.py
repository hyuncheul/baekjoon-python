'''다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. 
c는 1로, d는 2로, ..., C를 8로 바꾼다.
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.'''

dajangjo = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]
asccount = 0
desccount = 0
for i in range(8):
    if ascending[i] == dajangjo[i]:
        asccount += 1
for i in range(8):
    if descending[i] == dajangjo[i]:
        desccount += 1

if asccount == 8 : 
    print('ascending')

elif desccount == 8:
    print('descending')

else: print('mixed')