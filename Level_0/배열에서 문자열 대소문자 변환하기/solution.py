def solution(strArr):
    for s in range(0,len(strArr)):
        if s%2==0 : strArr[s] = strArr[s].lower()
        else : strArr[s] = strArr[s].upper()
    return strArr