import sys
def intervals(A,B):
    if B in A:
        print 1
        return 1
    i = 0
    j = len(A)-1
    start = -1
    end = -1
    maxv = -sys.maxint
    while i <len(A):
        if A[i][0] <= B[0]:
            if A[i][0] <= B[0] and A[i][1] >= B[1]:
                return 1
            elif A[i][0] <= B[0] and A[i][1] < B[1]:
                if maxv < A[i][1]:
                    maxv = A[i][1]
                    start = i
                i += 1
        else:
            i +=1
    i = len(A)-1
    minv  = sys.maxint
    while i >0:
        if A[i][0] <= B[1]:
           if A[i][0] <= B[1] and A[i][1] >= B[1]:
                if minv > A[i][1]:
                    minv = A[i][1]
                    end = i
           i -= 1

        else:
            i -=1
    dict = {i: sys.maxint for i in range(B[0], B[1] + 1)}
    for i in range(A[start][0],A[start][1]+1):
        dict[i] = 1
    print(dict)
    for i in range(start+1, end+1): # 6 21
        starti =A[i][0]                #6
        endi = A[i][1]                 #21
        for i in range(starti, endi):  #6 21
            if endi < len(dict):
                dict[endi] = min(dict[endi],1)
    print(dict)
    if B[1] < sys.maxint:
        return dict[B[1]]
    else:
        return 0

def find_min_intervals(intervals, target):
    intervals.sort()
    res = 0
    cur_target = target[0]
    i = 0
    max_step = 0
    while i < len(intervals) and cur_target < target[1]:
        if  i < len(intervals) and intervals[i][0] <= cur_target:
            check = True
        else:
            check = False
        while i < len(intervals) and intervals[i][0] <= cur_target:
            max_step = max(max_step, intervals[i][1])
            i += 1
        cur_target = max_step
        res += 1
        if check != True:
            i +=1
    return res if cur_target >= target[1] else 0
# (0,5) (4,20) (5,15) (5,22) (6,21) (7,12) (9,23) (13,25)
A = [[0,5],[5,12],[7,16],[4,14],[8,23],[23,25]]
B=[6,24]

print(find_min_intervals(A,B))



