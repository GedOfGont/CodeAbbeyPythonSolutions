secret_value, amount_values = map(int, input().split())
results = []
string_secret_value = str(secret_value)

def get_bulls_cows(guess):
    pair,contains = 0 , 0
    for i in range(len(guess)):
        for j in range(len(string_secret_value)):
            if(guess[i] == string_secret_value[j]):
                if(i == j):
                    pair += 1
                else:
                    contains += 1
    result = str(pair)+"-"+str(contains)
    return result

guess = input().split()
for i in range(amount_values):
    results.append(get_bulls_cows(guess[i]))

print(*results)


