import math

P, R, L = map(int, input().split())
R /= 1200

M = P*(R/(1-(1+R)**-L))

print(math.ceil(M))