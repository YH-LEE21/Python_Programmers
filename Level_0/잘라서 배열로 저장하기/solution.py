def my_strSlice(my_str, n):
    return [my_str[i: i + n] for i in range(0, len(my_str), n)]



print(my_strSlice("abc1Addfggg4556b"))
print(my_strSlice("abcdef123"))