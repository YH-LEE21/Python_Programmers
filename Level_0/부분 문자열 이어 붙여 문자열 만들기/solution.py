def solution(my_strings, parts):
    return "".join([my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(0,len(my_strings))])