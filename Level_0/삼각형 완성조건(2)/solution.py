def isTriangle2(sides):
    return len([i for i in range(1,sum(sides)) if i+min(sides) > max(sides)])