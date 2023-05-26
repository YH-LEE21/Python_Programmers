def solution(numLog):
    dict_wsda = {1: 'w' , -1 : 's', 10 : 'd', -10 : 'a'}
    return  ''.join([dict_wsda[numLog[i]-numLog[i-1]] for i in range(1,len(numLog))])