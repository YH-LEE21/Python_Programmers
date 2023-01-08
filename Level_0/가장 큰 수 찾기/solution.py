def searchMax(array):
    return [max(array),array.index(max(array))]

print(searchMax([1, 8, 3]))
print(searchMax([9, 10, 11, 8]))