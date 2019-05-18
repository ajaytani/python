def findEle(A,k, left=0, right=0):

    n = len(A)

    if left < right:
        return 0

    elif k < A[left]:
        return 0

    elif k > A[right]:
        return 0

    elif A[left] == k and A[right] == k:
        return right - left

    else:
        mid = (right + left) //2
        if A[mid] == k:
            return 1 + findEle(A,k,mid+1,right) + findEle(A,k,left,mid-1)
        elif A[mid] > k:
            return findEle(A,k,mid+1,right)
        elif A[mid] < k:
            return findEle(A,k,left, mid-1)


print (findEle([1,2,3,4,4,6,7,100,1212,2233],2233))