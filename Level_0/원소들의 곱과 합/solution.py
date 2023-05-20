from functools import reduce

def productAndSumOfTheElements(num_list):
    return 1 if sum(num_list)**2 > reduce(lambda x,y : x*y,num_list) else 0