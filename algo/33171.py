"""
Given a set of tasks like [A, A, B], and int k, which is the waiting time between two same tasks.
Calculate the min total execution time if you are allowed to rearrange the tasks.
Assume the execution for each individual task is 1.
In above example
A A B, k = 1, without rearrangement, the execution time would be 4:
Example A A A A A A A A A
Example 2 [A,A,B,C,C,C,B,D,A,D]
Example 3 BBBBBBAAAAAA
Example 4 A
Example 5 ABACBCBDEDE
"""

def counttaskweight(A):
    cnt = 0
    n = len(A)
    for i in range(n-1):
        if A[i] ==A[i+1]:
            cnt +=1
    print A
    print n + cnt
    return n + cnt

def rearrange(A):
    n = len(A)
    if n == 0:
        return
    if n == 1:
        return 1
    if n == 2:
        return counttaskweight(A)
#
    j = 0
    while j < n - 1 and A[j] == A[j + 1]:
        j += 1
    if j == n - 1:
        print A
        print 2*n-1
        return 2 * n - 1
    swapped = True
    i = n-1
    while i > 0:
        if A[i] == A[i-1]:
            i -=1
            j = i
            while j > 0 and A[j] == A[i]:
                j -=1
            if A[j] <> A[i]:
                A[i],A[j] = A[j],A[i]
                swapped = True
            elif j == 0:
                swapped = False
        if swapped == True:
            i -=1
        else:
            break

    st = 0
    nd = n-1
    while st <n-1:
        if A[st] == A[st+1]:
            st +=1
            nd = st
            while nd < n-1 and A[nd] ==A[st]:
                nd +=1
            if A[nd] != A[st]:
                A[st], A[nd] = A[nd], A[st]
                swapped = True
            elif nd == n-1:
                swapped =False
        if swapped == True:
            st += 1
        else:
            break
    return counttaskweight(A)
rearrange([1, 1, 1, 1,1, 2, 2, 3])
rearrange([1,1,1,1,1,1])
rearrange([1,2,1,3,3,3,4,5])
rearrange([1,1,1,3,3,3])
rearrange([4,6,5,3,3,3])
rearrange([1])




#check odd place
#return