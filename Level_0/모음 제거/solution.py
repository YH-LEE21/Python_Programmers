def removeVowels(my_string):
    answer = ''
    for i in 'a','e','i','o','u':
        my_string = my_string.replace(i,"")
    answer = my_string
    return answer

print(removeVowels("bus"))
print(removeVowels("nice to meet you"))
