amount_values = int(input())
results = []

def count_hand(values):
    sum = 0
    for i in values:
        if i in ['T', 'J', 'Q', 'K']:
            sum += 10
        elif i == 'A':
            sum += 1
        else:
            sum += int(i)
    if('A' in values and sum+10 < 22):
        sum += 10
    if(sum > 21):
        return "Bust"
    return sum

for i in range(amount_values):
    hand = list(map(str, input().split()))
    results.append(count_hand(hand))

print(*results)