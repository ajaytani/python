import sys
def coinChange(coins,target):

    T = [float('inf')]*(target+1)
    T[0] = 0

    for i in coins:
        for j in range(1,target +1):
            if j >=i:
                T[j] = min(T[j], 1+ T[j - i])
            print(T)

    return T[target]


print(coinChange([7,2,1,14],13))