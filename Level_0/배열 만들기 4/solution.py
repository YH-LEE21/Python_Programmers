def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if stk == []:
            stk.append(arr[i])
            i+=1
        else:
            r = stk[len(stk)-1]
            if arr[i] > r:
                stk.append(arr[i])
                i+=1
            else:
                stk.pop()
        
    return stk