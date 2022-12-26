import fractions
def addFractions(denum1, num1, denum2, num2):
    a = fractions.Fraction(denum1,num1)
    b = fractions.Fraction(denum2,num2)
    result = a+b
    return [result.numerator,result.denominator]

    
print(addFractions(1,2,3,4))
print(addFractions(9,2,1,3))
