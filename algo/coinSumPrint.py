def coinSum(coinList,Target):

    dp = [0]*(Target+1)

    for i in range(1,Target+1):
        for j in coinList:
            if i == j or dp[i-j] ==1:
                dp[i] = 1

    for i in range(Target+1):
        if dp[i] == 1:
            print i


coinSum([10,15,55],1000)

