def stringRepeat(my_string, n):
    answer = ""
    for i in my_string:
        answer += i*n
    return answer

print(stringRepeat("hello",3))