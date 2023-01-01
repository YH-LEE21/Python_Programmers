def clothesDC(price):
    answer = price
    if answer>= 500000:
        answer -= price*0.2
    elif answer >= 300000:
        answer -= price*0.1
    elif answer >= 100000:
        answer -= price*0.05
    return int(answer)

print(clothesDC(150000))
print(clothesDC(580000))
