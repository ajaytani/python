# assume both the arrays are sorted
#find element

def bsearch(A,e):
    l= len(A)
    if l ==0:
        return
    if l == 1:
        return A[0] == e
    else:
        for i in range(l):
            if A[l//2] == e:
                return l//2
            else 

def sortdualarrays(A1,A2,e):
    l1 = len(A1)
    l2 = len(A2)
    if A1[0] >= A2[l2-1]:
        if e > A1[0]:
            # search A2
            pass
    elif A2[0] >= A1[l1-1]:
        if e > A2[0]:
            # search A2
            pass
    else:
        pass
