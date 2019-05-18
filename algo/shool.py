def count(n):

    arr = [[]]
    arr[0].append(0)
    arr[0].append(1)
    arr[1][0] = 1
    arr[1][1] = 1

    print (arr)
    for i in range ( 2,n+1):
        arr[i % 2][0] = arr[(i-1) % 2][0] + arr[(i-1) % 2][1]#  // the ith letter is O
        arr[i % 2][1] = arr[(i-1) % 2][0] + arr[(i-2) % 2][0]#  // the ith letter is L

    opt = arr[n][0] + arr[n][1]#   // case when there is no "A"



    for i in range(n): #     // consider all the cases with one A, there are i letters to the left of A and n-i-1 letter to the right of A
        opt += ( arr[i][0] + arr[i][1] ) * ( arr[n-i-1][0] + arr[n-i-1][1] )

    return opt


print(count(3))