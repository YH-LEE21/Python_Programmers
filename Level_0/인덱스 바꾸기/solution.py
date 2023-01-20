def indexChange(my_string, num1, num2):
    answer = list(my_string)
    answer[num2] = my_string[num1]
    answer[num1] = my_string[num2]
    return "".join(answer)

print(indexChange("hello",1,2))
print(indexChange("I love you",3,6))