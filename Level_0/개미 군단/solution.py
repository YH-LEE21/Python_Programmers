def antCorps(hp):
    answer = 0
    ant5 = hp//5
    ant3 = (hp%5)//3
    ant1 = ((hp%5)%3)
    return ant5+ant3+ant1

print(antCorps(23))
print(antCorps(24))
print(antCorps(999))