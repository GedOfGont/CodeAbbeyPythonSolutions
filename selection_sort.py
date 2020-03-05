amount_values = int(input())
result = []

def selection_sort(values):
    for i in range(1,len(values)):
        max = 0
        last = len(values)-i
        for j in range(0,last+1):
            if(values[j] > values[max]):
                max = j
        values[last], values[max] = values[max], values[last]
        result.append(max)

values = list(map(int, input().split()))
selection_sort(values)
print(*result)