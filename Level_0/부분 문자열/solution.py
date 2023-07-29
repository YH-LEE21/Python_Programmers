def solution(str1, str2):
    answer = 0
    if str1.islower() and str2.islower():
        try :
            answer = str2.index(str1)
            return 1
        except:
            return 0
