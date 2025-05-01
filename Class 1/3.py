''' JavaScript에서 
$+, -$은 수에 대해서는 일반적인 의미의 덧셈 뺄셈의 의미를 가지고 있습니다. 하지만 문자열에 대해서 
$+$는 두 문자열을 이어붙이라는 의미이고, 
$-$는 양쪽 문자열을 수로 해석한 이후에 빼라는 의미입니다.

$A, B, C$를 각각 수와 문자열로 생각했을 때 
$A+B-C$를 출력하세요. '''

A = input()
B = input()
C = input()

inta = int(A)
intb = int(B)
intc = int(C)

res = A + B
res = int(res) - int(C)
intres = inta + intb - intc
print(intres)
print(res)