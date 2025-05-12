# Fizz 3의배수
# Buzz 5의배수
# FizzBuzz 15의 배수 

A = input()
B = input()
C = input()

if A not in ["Fizz", "Buzz", "FizzBuzz"]:
    A = int(A)
    D = A + 3
elif B not in ["Fizz", "Buzz", "FizzBuzz"]:
    B = int(B)
    D = B + 2
elif C not in ["Fizz", "Buzz", "FizzBuzz"]:
    C = int(C)
    D = C + 1

if D % 15 == 0:
    D = 'FizzBuzz'
elif D % 5 == 0:
    D = 'Buzz'
elif D % 3 == 0: 
    D = 'Fizz'

print(D)