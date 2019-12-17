def decode(value):
    binary_value = str("{0:b}".format(value))
    while(len(binary_value) < 8):
        binary_value = "0"+binary_value

    ones = 0
    for i in binary_value:
        if(i == "1"):
            ones += 1
    
    if(ones % 2 == 0):
        if(binary_value[0] == "0"):
            return chr(value)
        else:
            return chr(value-128)

    return ''

decode_string = ""
values = list(map(int, input().split()))

for i in values:
    decode_string += decode(i)
print(decode_string)