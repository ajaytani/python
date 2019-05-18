def print_roman(s):
    map ={'I': 1 ,'V': 5 ,'X': 10 ,'L': 50 ,'C': 100 ,'D': 500 ,'M': 1000 }
    sum = 0
    prev = None
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        val = map[c]
        if  prev:
            if prev > val:
                sum -= val
            else:
                sum += val
        else:
            sum += val
        prev = val
    return sum

print(print_roman('MCMXLVII'))