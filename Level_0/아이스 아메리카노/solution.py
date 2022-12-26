def ice_Americano(money):
    answer = [money//5500,money%5500]
    return answer

print(ice_Americano(5500))
print(ice_Americano(15000))
