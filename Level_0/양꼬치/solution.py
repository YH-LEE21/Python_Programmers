def bill(n, k):
    if 0<n<1000:
        if int(n/10)<=k<1000:  
            return format(n*12000+(k-n//10)*2000,",")
        else:
            return "error"
    return "error"
    
print(bill(10,3))
print(bill(64,6))
