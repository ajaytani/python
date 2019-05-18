def zeromatrix(A):
    m = len(A[0])
    n = len(A)
    rowzero = False
    colzero = False
    for i in range(m):
        if A[0][i] == 0:
            rowzero = True
            break
    for i in range(n):
        if A[i][0] == 0:
            colzero = True
            break
    for i in range(1,n):
        for j in range(1,m):
            if A[i][j] == 0:
                A[0][j] = 0
                A[i][0] = 0
    for i in range(m):
        if A[0][i] ==0:
            j = 1
            while j < n:
                A[j][i] = 0
                j += 1
    for j in range(n):
        if A[j][0] ==0:
            i = 1
            while i < m:
                A[j][i] = 0
                i += 1
    if rowzero:
        for i in range(m):
            A[0][i] = 0
    if colzero:
        for j in range(n):
            A[j][0] = 0

    return A


A = [[1,0,6,7],[4,7,8,9],[8,9,1,5]]
for i in zeromatrix(A):
    print (i)