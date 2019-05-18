def strCompression(S):

    l = len(S)
    if l ==0:
        return ''

    elif l ==1:
        return S + '1'

    last = S[0]
    cnt = 1
    res = ''

    for i in range(1,len(S)):

        if S[i] == S[i-1]:
            cnt +=1

        else:
            res = res + S[i-1] + str(cnt)
            cnt =1
    res = res + S[i-1] + str(cnt)

    if len(res) > l:
        return 'compression not possible'
    else:
        return res

    return res


print(strCompression('aabbccdsseeddff'))