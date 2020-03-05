amount_values = int(input())
results = []

def get_result(king_position, queen_position):
    king_file = king_position[0]
    queen_file = queen_position[0]

    king_rank = king_position[1]
    queen_rank = queen_position[1]

    if((king_file == queen_file) or (king_rank == queen_rank)):
        return "Y"
    elif(abs(ord(king_file)-ord(queen_file)) == abs(int(king_rank)-int(queen_rank))):
        return "Y"
    else:
        return "N"

for i in range(amount_values):
    king_position, queen_position = map(str,input().split())
    results.append(get_result(king_position, queen_position))

print(*results)