def alphabetRemove(my_string, letter):
    answer = my_string.replace(letter,"")
    # for i in my_string:
    #     if not i == letter:
    #         answer +=i
    return answer
print(alphabetRemove("abcdef","f"))
