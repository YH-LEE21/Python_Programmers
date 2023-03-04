def ctrl_Z(s):
    answer = 0
    s = s.split(" ")
    for i in range(0,len(s)):
        if s[i] == 'Z':
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    return answer

s = "1 2 Z 3"
# 4
print(ctrl_Z(s))

s = "10 20 30 40"
# 100
print(ctrl_Z(s))

s = "10 Z 20 Z 1"
# 1
print(ctrl_Z(s))

s = "10 Z 20 Z"
# 0
print(ctrl_Z(s))

s = "-1 -2 -3 Z"
# -3
print(ctrl_Z(s))
