def arraySearchMiddleNum(array):
    list.sort(array)
    return array[len(array)//2]

array = [1, 2, 7, 10, 11]
print(arraySearchMiddleNum(array))
array = [9,-1,0]
print(arraySearchMiddleNum(array))
