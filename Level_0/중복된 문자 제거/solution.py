#방법 1 메소드 활용
def charOfDuplicatesRemove1(my_string):
    return "".join(dict.fromkeys(my_string))

#방법 2 반복문 활용
def charOfDuplicatesRemove(my_string):
    answer = ''
    for i in my_string:
        if i not in answer :
            answer += i 
    return answer

print(charOfDuplicatesRemove1("people"))