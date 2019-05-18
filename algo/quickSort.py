def quickSelect(S,left,right,k):
    if left == right:
        return S[left]
    split = partition(S,left,right)
    length = split - left +1
    if length == k:
        return S[split]
    elif k < length:
        return quickSelect(S,left,split-1,k)
    else:
        return quickSelect(S,split+1, right,k-length)

def partition(S,left,right):
    pivot = S[left]
    leftMark  = left +1
    rightMark = right
    x = 0
    while True:
        print(x)
        while leftMark < right and S[leftMark] < pivot:
            x += 1
            leftMark +=1
        while rightMark > left and S[rightMark] > pivot:
            x += 1
            rightMark -=1
        if rightMark <= leftMark:
            break
        else:
            S[leftMark],S[rightMark] = S[rightMark], S[leftMark]
    S[left], S[rightMark] = S[rightMark], S[left]
    return rightMark

S = [3,2,41,5,6,43,56,43,1,4,88,5,31,34,67,23,1,212,456,7,5,53,3,12,324,53,2,3242,346,752,2,4,343]
l = len(S)
k = l//2
if l % 2 == 0:
    print((quickSelect(S,0,l-1,k) + quickSelect(S,0,l-1,k+1))/2)
elif l % 2 != 0:
    print(quickSelect(S, 0, l - 1, k+1))



