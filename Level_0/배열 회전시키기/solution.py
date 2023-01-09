from collections import deque
def turnArrayLR(numbers, direction):
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else :
        numbers.rotate(-1)
    return list(numbers)

print(turnArrayLR([1,2,3],"right"))
print(turnArrayLR([4, 455, 6, 4, -1, 45, 6],"left"))