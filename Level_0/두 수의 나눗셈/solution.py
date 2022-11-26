# 제한사항 확인 완료
def divisorOfTwoNumbers(num1, num2):
    if 0< num1<= 100 and 0< num2 <=100: 
        return int(num1/num2*1000)
    return "error"

#ex)
print(divisorOfTwoNumbers(3,2))
print(divisorOfTwoNumbers(7,3))
print(divisorOfTwoNumbers(1,16))
print(divisorOfTwoNumbers(0,14))


