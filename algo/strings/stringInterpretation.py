def stringInterpretation(S1):
    #if single digit return 1
    if len(S1) == 1 and int(S1) == 0:
        return 0
    if len(S1) == 1:
        return 1
    #if double digit return 0
    if len(S1) ==2 and int(S1) > 26:
        return 1

    if int(S1) <=26:
        return 1 + stringInterpretation(S1[1:])
    if '0' not in S1[1:3]:
        return stringInterpretation(S1[1:]) + stringInterpretation(S1[2:])
    else:
        return 1+ stringInterpretation(S1[2:])

# 5604
# print(stringInterpretation('1101'))
#aja ka

def combination(n):
    if int(n) <= 10:
        return 1
    if int(n) <= 26:
        return 2
    nstr = n
    first = int(n[:1])
    second = int(n[1:2])
    head = n[1:]
    if int(n) >= 100:
        tail = n[2:]
    else:
        tail = 0
    if first * 10 + second <= 26:
        return combination(head)+combination(tail)
    else:
        return combination(head)

print(combination('123123'))






