import itertools

def inorder(preorder):
    if not preorder:
        return []
    else:
        root = preorder[0]
        left = []
        for i in preorder[1:]:
            if i < root:
                left.append(i)#list(itertools.takewhile(lambda x: x < root, preorder[1:]))
        right = preorder[len(left) + 1:]
        return inorder(left) +  [root] + inorder(right)

def findDiffPair(arr1Sorted,arr2Sorted,l1,l2):
    for i in range(max(l1,l2)):
        diff = 0
        if l1 != l2:
            diff = abs(l1 - l2)

        if (l1-diff > i or l2-diff > i) and arr1Sorted[i] != arr2Sorted[i]:
            return arr1Sorted[i], arr2Sorted[i]




if __name__ == '__main__':
    preorder = [5,4,2,4,8,6,9]
    arr1Sorted = inorder(preorder)
    preorder = [5,3,2,4,8,7,9]
    arr2Sorted = inorder(preorder)
    l1 = len(arr1Sorted)
    l2 = len(arr2Sorted)
    print(findDiffPair(arr1Sorted,arr2Sorted,l1,l2))