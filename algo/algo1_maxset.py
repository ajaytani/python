class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        n = len(A)
        low = 0
        high = n-1
        firstOcc = -1
        while low <= high:
            mid = (low+high)/2
            if A[mid] == B:
                firstOcc = mid
                high = mid - 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        if firstOcc == -1:
            return [-1,-1]
        low = firstOcc
        high = n-1
        secondOcc = -1
        while low <= high:
            mid = (low+high)/2
            if A[mid] == B:
                secondOcc = mid
                low = mid + 1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1
        return [firstOcc, secondOcc]

A= [3,3,4,4,4,5]
B= 4
x = Solution()
print (x.searchRange(A,B))