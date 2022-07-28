def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

"""반복문을 이용한 계산은 함수 호출로 인해
시스템 스택을 사용하지 않으므로 순환을 이용한 계산보다
매우 간단하며 메모리도 적게 사용함"""

fact =1
for i in range(1,5):
    fact *= i

print(fact)
