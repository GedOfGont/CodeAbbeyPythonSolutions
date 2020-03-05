values = list(map(int, input().split()))
results = []

def shuffle(shuffle_nums):
    
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    suits = ['C', 'D', 'H', 'S']

    cards = [i+j for i in suits for j in ranks]

    card = 0
    for shuffle_num in shuffle_nums:
        shuffle_num %= 52
        cards[card], cards[shuffle_num] = cards[shuffle_num],cards[card]
        card += 1

    print(*cards)

shuffle(values)
