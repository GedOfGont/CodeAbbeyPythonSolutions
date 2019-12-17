from math import sqrt

amount_values = int(input())
results = []

def get_roots(A,B,C):
    root = B**2-4*A*C

    if(root < 0):
        root *= -1
        x1 = str(-B//(2*A))+"+"+str(int(sqrt(root)/(2*A)))+"i"
        x2 = str(-B//(2*A))+"-"+str(int(sqrt(root)/(2*A)))+"i"
        
    else:
        x1 = int((-B + sqrt(root))/(2*A))
        x2 = int((-B - sqrt(root))/(2*A))

    return str(x1)+" "+str(x2)

for i in range(amount_values):
    A,B,C = map(int, input().split())
    results.append(get_roots(A,B,C))

print(*results, sep="; ")
