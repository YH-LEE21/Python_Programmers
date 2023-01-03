def numberAdd(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit()==True:
            answer += int(i)
    return answer

print(numberAdd("aAb1B2cC34oOp"))
print(numberAdd("1a2b3c4d123"))
