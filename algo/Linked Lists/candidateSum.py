def candidateSum(arr, target):
    output = set()
    if target in arr:
        output.add((target))

    n = len(arr)
    i = 0
    k = 0
    j = 0
    while i < n:
        check = target - (arr[i] + k)
        if check in arr:
            a2 = sorted([arr[i],check,k])
            a1 = sorted([arr[i], check])
            print (a1)
            if k == 0:
                output.add((a1[0],a1[1]))
            else:
                output.add((a2[0],a2[1],a2[2]))
        if i == n-1 and k != arr[n-1]:
            i = 0
            j += 1
            k = arr[j]
        i +=1
    print output



def printSum(candidates,lst,n):
    for i in range(n):
        
        print(candidates[lst[i]])



def solve(target, total, candidates,sz,lst,n):
    if total > target:
        return
    if target == total:
        printSum(candidates,lst, n )
    for i in range(sz):
        lst.append(i)
        solve(target, total + candidates[i], candidates, sz, lst, n + 1)

def candidateSum2(arr,target):
    output = set()
    lst = [0]
    if target in arr:
        output.add((target))
    solve(target, 0, arr,len(arr),lst,0)



candidateSum2([10, 1, 2, 7, 6, 1, 5],8)
