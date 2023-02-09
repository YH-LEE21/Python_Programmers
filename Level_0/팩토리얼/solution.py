def factorial(n):
    factorial = 1
    answer = 0
    for i in range(1,11):
        factorial = factorial * i
        if factorial <= n:
            answer = i
    return answer

print(factorial(3628800))
print(factorial(7))