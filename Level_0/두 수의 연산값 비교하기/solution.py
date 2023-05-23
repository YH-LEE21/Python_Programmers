def solution(a, b):
    str_a = str(a)
    str_b = str(b)
    answer = max(int(str_a+str_b),2*a*b)
    return answer