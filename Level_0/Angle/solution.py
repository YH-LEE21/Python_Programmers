def angleDistinction(angle):
    if angle%90 == 0:
        return 2 if angle==90 else 4
    else:    
        return 1 if angle<90 else 3

print(angleDistinction(70))#1
print(angleDistinction(91))#3
print(angleDistinction(180))#4