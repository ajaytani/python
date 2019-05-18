def intervalTimeCheck(A):
    dp = {}
    for i in A:
        for j in range(i[0],i[1]):
            dp[j] = 1

    return len(dp)

A = [[1,4], [6,8], [2,4], [7,9], [10, 15]]

print(intervalTimeCheck(A))