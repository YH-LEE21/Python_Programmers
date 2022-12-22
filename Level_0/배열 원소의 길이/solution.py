def arrayValueLengths(strlist):
    answer = [len(i) for i in strlist]
    return answer

strlist = ["We", "are", "the", "world!"]
print(arrayValueLengths(strlist))

strlist = ["I", "Love", "Programmers."]
print(arrayValueLengths(strlist))
