#create a BST from sorted array
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createBST(A,start,end):

    if start > end:
        return None

    mid =  (start+end)//2
    root = Node(A[mid])

    root.left =  createBST(A,start,mid-1)
    root.left = createBST(A, mid+1, end)

    return root

def isBST(root,minv,maxv):

    if not root:
        return True

    if root.data <minv or root.data> maxv :
        return False

    return isBST(root.left,minv,root.data) and isBST(root.right, root.data,maxv)