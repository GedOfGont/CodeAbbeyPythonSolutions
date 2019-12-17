amount_values = int(input())
results = []

def factorial(number):
    if(number < 1):
        return 1
    return number*factorial(number-1)

def get_combination(N,K):
    if(K == 0):
        return 1
    diff = N-K

    multipy = 1
    for i in range(N - min(diff, K)+1, N+1):
        multipy *=i
    fact = factorial(min(diff,K))
    result = multipy//fact
    return result
    
for i in range(amount_values):
    N,K = map(int, input().split())
    results.append(get_combination(N,K))

print(*results)
    
