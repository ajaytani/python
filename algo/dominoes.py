def dominoes(A):
    n = len(A)
    reach = 0
    Ans = [0]*n
    cascade = []
    for i in range(n):
        if A[i] != 0 and (i<=reach or reach == 0):
            Ans[i] = A[i] + i
            if A[i] + i > reach or reach == 0:
                cascade.append(i)
            reach = max(A[i] + i, reach)
        else:
            Ans[i] = A[i] + i
    print(cascade)
    for i in cascade:
        Ans[i] = reach
    print Ans

dominoes([0,0,4,1,0,2,0,1,0,0,3])

