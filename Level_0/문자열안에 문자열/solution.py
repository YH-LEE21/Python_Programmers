def findWords(str1, str2):
    if str1.find(str2) != -1:
        return 1
    else :
        return 2

str1 = "ab6CDE443fgh22iJKlmn1o"	
str2 = "6CD"
print(findWords(str1,str2))

str1 = "ppprrrogrammers"
str2 = "pppp"
print(findWords(str1,str2))
