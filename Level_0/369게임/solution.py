def game369(order):
    order = str(order)
    return order.count('3')+order.count('6')+order.count('9')

print(game369(3))
print(game369(29423))