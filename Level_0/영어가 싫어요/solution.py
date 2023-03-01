def hate_English(numbers):
    dic_Num = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    for key in dic_Num.keys():
        numbers = numbers.replace(key,str(dic_Num[key]))
    return int(numbers)

#123456789
print(hate_English("onetwothreefourfivesixseveneightnine"))

#14067
print(hate_English("onefourzerosixseven"))