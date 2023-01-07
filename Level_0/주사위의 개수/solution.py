def theNumberOfDice(box, n):
    return (box[0]//n)*(box[1]//n)*(box[2]//n)  
box = [1,1,1]
n = 1
print(theNumberOfDice(box,n))

box = [10,8,6]
n = 3
print(theNumberOfDice(box,n))
