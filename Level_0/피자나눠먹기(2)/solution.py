def pizza_divide2(n):
    return min([i//6 for i in range(6,607,6) if i%n==0])

print(pizza_divide2(6))
print(pizza_divide2(10))
print(pizza_divide2(4))