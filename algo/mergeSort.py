def mergeSort(arr):

    if len(arr) > 1:
        n = len(arr)
        mid = n//2
        right = arr[:mid]
        left = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        #merge operation
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i +=1

            else:
                arr[k] = right[j]
                j +=1
            k +=1

        while i < len(left):
            arr[k] = left[i]
            i +=1
            k +=1

        while j < len(right):
            arr[k] = right[j]
            j +=1
            k +=1



arr = [9,2,43,1,4,5,23,]
mergeSort(arr)
print(arr)




