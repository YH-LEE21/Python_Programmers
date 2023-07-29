def solution(my_string, target):
    answer = 0
    if my_string.islower() and target.islower():
        try :
            answer = my_string.index(target)
            return 1
        except:
            return 0
    
