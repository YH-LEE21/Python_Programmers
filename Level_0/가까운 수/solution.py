def nearNum(array, n):
    array.sort()
    answer = [abs(n-i) for i in array]
    return array[answer.index(min(answer))]

print(nearNum([3, 10, 28],20))
print(nearNum([10,11,12],13))