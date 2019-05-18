import random
def pickRandom(arr,freq):
        sums = [0]*len(arr)
        randValue = 0
        sum = 0
        randIndex = 0
        for i in range(len(arr)):
            sums[i] = sum + freq[i]
            randValue += random.randint(0,freq[i] + 1)
            sum += freq[i]
            while(randIndex < (len(arr) - 1) and randValue >= sums[randIndex] and randIndex <= i ):
                randIndex+=1
        return arr[randIndex]


print(pickRandom([1,7,7,3,4,6,9,2,0,20],[1,2,2,1,1,1,1,1,1,1]))