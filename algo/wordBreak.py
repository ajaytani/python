def wordBreak(s,wordDict):
    n = len(s)
    if not s or n== 0:
        return False

    dp = [[] for i in range(n+1)]
    dp[0] = [0]

    for i in range(1,n+1):
        for j in range(i):
            if s[j:i] in wordDict:
                dp[i].append(j)
    print dp
    res = []
    backTracking(dp,s,n,res,'')
    return res

def backTracking(dp,s,idx,res,line):
    for i in dp[idx]:
        print 'line : ' + line
        print 'idx : ',idx
        print 'dp[idx] ', dp[idx]
        newline = s[i:idx] + ' ' + line if line else s[i:idx]
        print 'newline : ' + newline
        if i == 0:
            res.append(newline)
        else:
            print 'backtracking call:' + newline
            backTracking(dp,s,i,res,newline)


s = 'catsanddogcat'
wordDict = ['cat','cats','and','sand','dog']

print(wordBreak(s,wordDict))

