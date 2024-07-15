import math
a =  float(input())
b =  float(input())
c =  float(input())

formula = b**2 -4*a*c

if formula > 0:
    root1 = (-b + formula**0.5) / 2*a
    root2 = (-b - formula**0.5) / 2*a
    print(f"roots are: {root1} and {root2}")
elif formula == 0:
    root1 = root2 = -b / 2*a
    print(f"roots are: {root1} and {root2}")
else:
    realPart = -b / 2*a
    imaginaryPart = ( math.sqrt(abs(formula)) / 2*a)
    print(f"roots are: {realPart} + {imaginaryPart}i and {realPart} - {imaginaryPart}i")
