
def splitBySum(arr):

    sumv = sum(arr)
    currTotal = 0
    for i in range(len(arr)):

        if sumv/2 == currTotal + arr[i]:
            return arr[0:i+1] ,arr[i+1:len(arr)]

        elif currTotal + arr[i] <sumv/2:
            currTotal +=arr[i]

        else:
            return False


arr=[[1,2,3,3,2,1],[1,2,3,4,5,6,21],[1,90, 50, 30, 5, 3, 2, 1 ],[50, 50, 900, 1000 ]]
for test in arr:
    print splitBySum(test)