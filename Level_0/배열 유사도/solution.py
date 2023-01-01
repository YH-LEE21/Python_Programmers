def arrayResemblance(s1, s2):
    answer = 0
    for i in s1:
        answer += s2.count(i)
    return answer

print(arrayResemblance(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(arrayResemblance(["n", "omg"],["m", "dot"]))
