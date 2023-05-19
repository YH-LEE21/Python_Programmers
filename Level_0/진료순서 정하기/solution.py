def clinicPriority(emergency):
    #enumerate는 배열에서 index,value 동시에 가져 올 수 있으므로 다양하게 활용가능하다
    dict = {num: index for index, num in enumerate(sorted(emergency, reverse=True), start=1)}
    return [dict[i] for i in emergency]

print(clinicPriority([3, 76, 24]))
print(clinicPriority([1, 2, 3, 4, 5, 6, 7]))
print(clinicPriority([30, 10, 23, 6, 100]))
