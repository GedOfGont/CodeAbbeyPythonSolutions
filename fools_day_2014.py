amount_values = int(input())
results = []

def get_square_sum(values):
    square_sum = 0
    for i in values:
        square_sum += i**2
    return square_sum

for i in range(amount_values):
    values = list(map(int,input().split()))
    results.append(get_square_sum(values))

print(*results)
