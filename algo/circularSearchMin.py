def circularSearchMin(A, left, right):

     n = len(A)

     if A[left] == [right]:
         return

     if left < right:
         return A[0]

     else:
         left = 0
         right = n-1
         mid = (left + right) //2

[4,7,9,11,12,1,2]

mid = 9
