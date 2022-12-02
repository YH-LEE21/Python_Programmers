def taller_Than_Me(array, height):
    return len([ i for i in array if i>height])

print(taller_Than_Me([149, 180, 192, 170],167))
print(taller_Than_Me([180, 120, 140],190))
