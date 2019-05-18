#boolean rotate(int[][] matrix) { 2 if (matrix.length == 0 I I matrix. length != matrix[0].length) return false;
#  int n = matrix. length;
# for (int layer = 0; layer < n / 2; layer++) { 5 int first = layer; 6 int last = n - 1 - layer; 7 for(int i = first; i < last; i++)
# { 8 int offset = i-first;

def rotate(matrix):
    if len(matrix) !=len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        print ('layer: ', layer)
        first = layer
        last = n - 1 - layer
        for i in range(first,last):
            print(i)
            offset = i - first
            #assign top to a value
            matrix[first][i], matrix[last - offset][first], matrix[last][last - offset], matrix[i][last] = \
            matrix[last - offset][first], matrix[last][last - offset], matrix[i][last], matrix[first][i]
    return matrix



def spiralPrint(matrix):

    m = len(matrix)
    n = len(matrix[0])
    topRow = 0
    btmRow = m - 1
    leftCol = 0
    rightCol = n - 1

    while topRow <= btmRow and leftCol <= rightCol:
        # print the next top row
        for i in range(leftCol, rightCol+1):
            print (matrix[topRow][i])
        print('\n')
        topRow +=1

        # print the next right hand side column
        for i in range(topRow,btmRow+1):
            print (matrix[i][rightCol])
        print('\n')
        rightCol -=1

        # print the next bottom row
        # print(btmRow,rightCol,leftCol)
        if topRow <= btmRow:
            for i in range(rightCol, leftCol-1,-1):
                # print(btmRow,i)
                print matrix[btmRow][i]
            btmRow -=1

        # print the next left hand side column
        if leftCol <= rightCol:
            for i in range(btmRow, topRow-1,-1):
                print matrix[i][leftCol]
            leftCol +=1

spiralPrint([[1,4,2,5],[3,4,7,4],[9,6,3,1],[0,-1,7,9]])
# print(rotate([[1,4,2,5],[3,4,7,4],[9,6,3,1],[0,-1,7,9]]))
"""
0 to 2:
n = 4
layer = 0
first = 0 last 4-1-0 = 3

first = 0, i = first to last  =0
offset =0-0 =0

m[0][0], m[3][0],m[3][3], m[0][3] = m[3][0],m[3][3],m[0][3],m[0][0]
1,0,9,5 = 0,9,5,1
    1  4  2  5
    3  4  7  4
    9  6  3  1
    0 -1  7  9

"""







