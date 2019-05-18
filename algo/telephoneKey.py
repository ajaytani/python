#given a number say 633 4263 return all the words by input num;ber using telephonic keyboard
hashlist = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
def telephoneKeys(N,curr_digit,output,ln):
    if curr_digit == ln:
        # print output
        print(''.join(output))
        return
    for i in range(len(hashlist[int(N[curr_digit])])):
        if len(output)  > curr_digit:
            output[curr_digit] = hashlist[int(N[curr_digit])][i]
        else:
            output.append(hashlist[int(N[curr_digit])][i])
        print(output)
        telephoneKeys(N, curr_digit+1, output, ln)

        if N[curr_digit] ==0 or N[curr_digit] == 1:
            return
telephoneKeys('6334263', 0, [],7)


def wordBreak(S1,wordDict):
    n = len(S1)
    dp = [[] for i in range(n+1)]
    dp[0] = [0]
    if len(S1) == 0:
        return

    else:
        for i in range(1,n+1):
            for j in range(i):
                if S1[j:i] in wordDict:
                    dp[i].append(j)
    res =[]
    backTrack(S1,dp,res,n,'')
    return res

def backTrack(S,dp,res,idx,line):

    for i in dp[idx]:
        newline = S[i:idx] + ' ' + line if line else S[i:idx]
        if i == 0:
            res.append(newline)
        else:
            backTrack(S,dp,res,i,newline)



#
# s = 'ilikefacebook'
# wordDict = ['ok','like','face','book','facebook','i']
#
# print(wordBreak(s,wordDict))


