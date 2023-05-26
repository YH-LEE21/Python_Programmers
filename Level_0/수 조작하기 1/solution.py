def solution(n, control):
    dict_wsda = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    return n + sum([dict_wsda[i] for i in control])