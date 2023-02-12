def array2(num_list, n):
    return [num_list[i:i+n] for i in range(0,len(num_list),n)]

print(array2([1, 2, 3, 4, 5, 6, 7, 8],2))
print(array2([100, 95, 2, 4, 5, 6, 18, 33, 948],3))
