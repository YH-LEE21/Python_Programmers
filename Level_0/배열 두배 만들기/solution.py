def arrayValuesDouble(numbers):
    answer = [i*2 for i in numbers]
    return answer

numbers = [1,2,3,4,5]
print(arrayValuesDouble(numbers))

numbers = [1,2,100,-99,1,2,3]
print(arrayValuesDouble(numbers))
