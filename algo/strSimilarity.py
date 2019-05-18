# 1
# Set n to be the length of s.
# Set m to be the length of t.
# If n = 0, return m and exit.
# If m = 0, return n and exit.
# Construct a matrix containing 0..m rows and 0..n columns.
# 2
# Initialize the first row to 0..n.
# Initialize the first column to 0..m.
# 3
# Examine each character of s (i from 1 to n).
# 4
# Examine each character of t (j from 1 to m).
# 5
# If s[i] equals t[j], the cost is 0.
# If s[i] doesn't equal t[j], the cost is 1.
# 6
# Set cell d[i,j] of the matrix equal to the minimum of:
# a. The cell immediately above plus 1: d[i-1,j] + 1.
# b. The cell immediately to the left plus 1: d[i,j-1] + 1.
# c. The cell diagonally above and to the left plus the cost: d[i-1,j-1] + cost.
# 7
# After the iteration steps (3, 4, 5, 6) are complete, the distance is found in cell d[n,m].
#if substituion is allowed below algo works else it will be longest common sub sequence where if letter matches get diagonal +1 else get max(left[i-1][j] and top[i][j-1]) track max value and return


def LevenshteinDistance(s1, s2):

    s1len = len(s1)
    s2len =  len(s2)
    if s1len ==0:
        return s2len
    if s2len ==0:
        return s1len

    column = []

    column.append([x for x in range(s2len+1)])


    for i in range(1,s1len+1):
        column.append([i] + [0 for x in range(s2len)])
    for i in range(1,s1len+1):
        for j in range(1,s2len+1):
            if s1[i - 1] == s2[j - 1]:
                column[i][j] = column[i-1][j-1]
            else:
                column[i][j] = min (column[i-1][j],column[i][j-1],column[i-1][j-1]) +1

    return column[s1len][s2len]
print(LevenshteinDistance('azced','abcdef'))