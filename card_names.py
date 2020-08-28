amount_values = int(input())

results = []

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

def get_card_name(card_value):
    suit_value = suits[card_value//13]
    rank_value = ranks[card_value%13]

    return rank_value+"-of-"+suit_value

card_values = list(map(int, input().split()))
for i in range(amount_values):
    results.append(get_card_name(card_values[i]))

print(*results)