def oneAlphabet(s):
    dict = {i : 0 for i in set(s)}
    for i in s:
        dict[i]+=1
    return "".join(sorted([i for i in set(s) if dict[i] == 1]))

print(oneAlphabet("abcabcadc"))
print(oneAlphabet("abdc"))
print(oneAlphabet("hello"))