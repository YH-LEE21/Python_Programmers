def isTriangle(sides):
    list.sort(sides)
    return 2 if sides[2] >= sides[0]+sides[1] else 1