def location_Player(keyinput, board):
    dic = {
        "left" : (-1,0),
        "up" : (0,1),
        "down" : (0,-1),
        "right" : (1,0),
    }
    x,y = 0,0
    lr, ud = board
    lr//=2
    ud//=2
    for key in keyinput:
        dx,dy = dic[key]
        x += dx
        y += dy
        x=max(-lr,x)
        y = max(-ud,y)
        x = min(lr,x)
        y = min(ud,y)
    answer = [x,y]
    return answer