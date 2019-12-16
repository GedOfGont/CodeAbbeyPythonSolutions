from math import ceil

amount_values = int(input())
results = []

def get_min_printig_time(printer1, printer2, page_number):

    time1 = ceil(max(printer1,printer2)/(printer1+printer2)*page_number)*min(printer1, printer2)
    time2 = ceil(min(printer1,printer2)/(printer1+printer2)*page_number)*max(printer1, printer2)
    return min(time1,time2)

for i in range(amount_values):
    printer1, printer2, page_number = map(int, input().split())
    results.append(get_min_printig_time(printer1, printer2, page_number))

print(*results)
