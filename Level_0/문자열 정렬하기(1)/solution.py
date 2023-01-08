def strNumSort(my_string):
    return sorted([int(i) for i in my_string if i.isdigit() == True])

print(strNumSort("hi2392"))
print(strNumSort("p2o4i8gj2"))
print(strNumSort("abcde0"))