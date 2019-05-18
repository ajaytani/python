def mergeIntervals(int1, int2):
    if not int1 or not int2:
        return int1 or int2
    ret = []
    i = 0
    j = 0
    if int1[0][0] < int2[0][0]:
        curr = int1[0]
        i = 1
    else:
        curr = int2[0]
        j = 1

    while i < len(int1) or j < len(int2):
        if j == len(int2) or int1[i][0] < int2[j][0]:
            nxt = int1[i]
            i += 1
        else:
            nxt = int2[j]
            j += 1
        if curr[1] < nxt[0]:
            ret.append(curr)
            curr = nxt
        else:
            curr[1] = max(curr[1], nxt[1])
    ret.append(curr)

    return ret


A= [1,5], [10,14], [16,18]
B= [2,6], [8,10], [11,20]

print(mergeIntervals(A,B))
