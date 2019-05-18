def quicksort(A):
    quicksort_help(A, 0, len(A)-1)

def quicksort_help(A,first,last):
    if first < last:

        splitpoint = partition(A,first,last)

        quicksort_help(A,first,splitpoint-1)
        quicksort_help(A, splitpoint + 1,last)

def partition(A,first,last):

    pivotvalue = A[first]

    i = first + 1
    j = last

    done = False
    while not done:
        while A[i] <= pivotvalue and  i <=j:
            i += 1
        while A[j] >= pivotvalue and  i <=j:
            j -= 1
        if j < i:
            done = True
        else:
            #swap values at left that are high with values low on right
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            print (A)
    #pivot value swap below
    temp = A[first]
    A[first] = A[j]
    A[j] = temp
    print('pivot swap:',A)
    return j

arr = [3,4,2,1,5,2,6,7,2,2,111,-1]
quicksort(arr)
print(arr)