from math import sqrt

amount_values = int(input())
results = []

def sieve(limit):
    prime_numbers = []
    numbers = list(range(limit))
    for i in range(2, int(sqrt(limit))):
        for j in range(i*i, limit, i):
            numbers[j] = -1
            
    for i in numbers:
        if(i not in [-1,0,1]):
            prime_numbers.append(i)


    return prime_numbers

prime_numbers = sieve(2750160)
values = list(map(int, input().split()))

for i in range(amount_values):
    results.append(prime_numbers[values[i]-1])


print(*results)

