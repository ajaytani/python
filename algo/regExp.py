def regExp(s,p):
    i = j = 0
    x = 0
    y = -1
    m = len(s)
    n = len(p)

    while i < m:
        if j < n and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
# if element doesnt match and pattern is not '?' then pattern should be '*'
        elif j < n and (p[j] == '*'):
            x = i
            y = j
            j +=1
# as it hits a  * in the previous iteration y >= 0 condition will be hit, once it hits this its always true
        elif y >=0:
            i = x + 1
            x += 1
            j = y
        else:
            return False

    if i != m:
        return False
#ends with multiple * like *****
    while j < n and p[j] == '*':
        j += 1

# both i and j should be incremented if not it j is not at the end it means we havent found a complete match
    return j == n

print (regExp('xay','x?b'))

