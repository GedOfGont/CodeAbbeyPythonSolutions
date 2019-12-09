amount_values = int(input())

def get_checksum(values):
    limit = 10000007
    result = 0
    seed = 113

    for i in values:
        result = (result + i) * seed
        if(result > limit):
            result = result % limit

    return result

values = list(map(int, input().split()))

print(get_checksum(values))
