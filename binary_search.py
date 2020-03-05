from math import sqrt
from math import exp

amount_values = int(input())
results = []

def solve_equation(A,B,C,D,x):
    return A*x+B*sqrt(x**3)-C*exp(-x/50)-D

def get_root(A,B,C,D):

    high = 100
    low = 0
    x = (high+low)/2
    result = solve_equation(A, B, C, D,x)

    while(result > 0.0000001 or result < 0.0000000):
        if(result > 0):
            high = x
        
        elif(result < 0):
            low = x
        
        x = (high+low)/2
        result = solve_equation(A, B, C, D,x)
    return(x)

for i in range(amount_values):
    A,B,C,D = map(float, input().split())

    results.append(get_root(A,B,C,D))

print(*results)
