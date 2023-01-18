def alienPlanetAge(age):
    return "".join(chr(97+int(i)) for i in str(age))

print(alienPlanetAge(23))
print(alienPlanetAge(51))
print(alienPlanetAge(100))