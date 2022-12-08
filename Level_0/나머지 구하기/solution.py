def divisor(num1,num2):
    if 0<num1<=100 and 0<num2<=100:
        return num1%num2
    return "Error!! num1 : 1~100, num2 : 1~100"

print(divisor(3,2))
print(divisor(10,5))
print(divisor(0,2))#"Error!! num1 : 1~100, num2 : 1~100"
