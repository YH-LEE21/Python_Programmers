def whereIsXY(dot):
    answer = 0
    if dot[0]*dot[1] > 0 :
        if dot[1]> 0:
            answer = 1
        else:
            answer = 3
    else:
         if dot[1]> 0:
            answer = 2
         else:
            answer = 4  
    return answer