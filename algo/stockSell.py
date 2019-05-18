def stockSell(prices,fees):
    if len(prices) <= 1:
        raise 'Error, No prices listed to check'
    maxprofitfinal = 0
    seen = 0
    maxset = []
    for i in range(len(prices)-1):
        maxprofit = 0
        for j in range(i+1,len(prices)):
            print (i,j, prices[j]-prices[i])
            if prices[j] - prices[i] > 0:
                maxset.append((i,j,prices[j] - prices[i]))

    return maxset


print stockSell([1, 10, 1, 7, 1, 4 ], 3)
