def stringCombination(S):
    output = ['']*len(S)
    countMap = {}
    i = 0
    k = 0
    uString = []
    while i < len(S):
        if S[i] in countMap:
            countMap[S[i]] +=1
        else:
            uString.append(S[i])
            countMap[S[i]] = 1
        i +=1
    cnt = []
    print(uString)
    for i in range(len(uString)):
         cnt.append(countMap[uString[i]])
    print ('call: S: {}, cnt: {}, out: {}, i: 0,length: 0'.format(uString, cnt, output))
    combinations(uString,cnt,output,0,0)

def combinations(S,cnt,out,pos,length):
    print(''.join(out[:length]))

    for i in range(pos,len(S)):
        if cnt[i] ==0:
            continue
        out[length]= S[i]
        cnt[i] -=1
        print ('call: S: {}, cnt: {}, out: {}, i: {},length: {}'.format(S,cnt,out,i,length+1) )
        combinations(S,cnt,out,i,length+1)
        print(cnt,pos)
        cnt[i] +=1

stringCombination('AABC')
