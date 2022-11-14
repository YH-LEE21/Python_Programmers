def sum_digit(number):
    return sum([int(i) for i in str(number)])
    
print(sum_digit(123))
print(sum_digit(987))
