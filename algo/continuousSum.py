def continuousSum(A,T):

    n = len(A)
    dict = {}
    total = 0
    start = 0
    for j in range(len(A)):
        if total == T:
            return True
        elif total < T:
            total += A[j]
        else:
            total +=A[j]
            while total > T:
                total -=A[start]
                start +=1
    if total == T:
        return True
    else:
        return False

print(continuousSum([5,4,3,2,5,5,7],22))