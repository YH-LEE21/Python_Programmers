#로마 숫자 숫자로 변형하기   ex) IV : 4 , XII : 12
roma_num = {'I':1, 'V':5, 'X':10}
def romaNum_REVERT(n):
    plus = 0
    for i in range(len(n)):
        for k in roma_num.keys():
            if n[i] == k:
                plus += roma_num[k]
                if n[i] == 'V' or n[i] == 'X':
                    x = i-1
                    if x < 0:
                        pass
                    elif n[x] == 'I':
                        plus -= 2
    return plus
#IV = 4 
print(roman("XX"))

