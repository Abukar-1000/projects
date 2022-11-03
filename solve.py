from fractions import Fraction
import math

def func(x):
    return math.sin(x**(.5))

deltaX = 2   
values = [1,3,5,7]

def solve():
    result = [func(x) for x in values]
    total = sum(result)
    print(f"result: {result}")
    return (str(Fraction(deltaX*total)),deltaX*total)
    
    
print(solve())

print(49/16)
