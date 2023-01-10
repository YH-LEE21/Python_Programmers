def maximumMade2(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])

print(maximumMade2([1,2,-3,4,-5]))
print(maximumMade2([0, -31, 24, 10, 1, 9]))
print(maximumMade2([10, 20, 30, 5, 5, 20, 5]))