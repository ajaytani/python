class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        k = 0
        n = len(A)
        if n == 0:
            return A
        for i in range(n):
            if A[i] == B:
                k += 1
            elif k > 0:
                print (A)
                A[i-k] = A[i]
        print (A)
        A = A[:n-k]
        print (A)
        return n - k

A= [3,3,4,4,4,5,4,4,3]
B= 4
x = Solution()
print (x.removeElement(A,B))