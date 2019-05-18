def number_needed(a, b):
    seen ={}
    for i in a:
        if i in seen:
            seen[i] +=1
        else:
            seen[i] = 1
    for j in b:
        if j in seen:
            seen[j] -=1
        else:
            seen[j] = 1
    cnt = 0
    for i in seen:
        cnt +=seen[i]
        
    return cnt

a = 'apple'
b = 'mkijn'
print(number_needed(a,b))