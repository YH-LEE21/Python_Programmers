def prime_factors(n):
    answer = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            answer.append(i)
    if n > 1:
        answer.append(n)
    return sorted(list(set(answer)))

print(prime_factors(12))

print(prime_factors(17))

print(prime_factors(420))

