import collections
import sys

class Node(object):

    def  __init__(self,value):
        self.root = None
        self.value = value
        self.left = None
        self.right = None

def levelOrderPrint(tree):

    if not tree:
        return

    nodes = collections.deque([tree])
    currentcount = 1
    nextcount = 0

    while len(nodes) != 0:

        currentnode = nodes.popleft()
        currentcount -=1

        print currentnode.value,

        if currentnode.left:
            nodes.append(currentnode.left)
            nextcount +=1

        if currentnode.right:
            nodes.append(currentnode.right)
            nextcount +=1

        if currentcount == 0:
            print '\n'
            currentcount,nextcount = nextcount,currentcount


def RootToLeaf(root,sumv,res=[]):

    if not root:
        return False
    if not root.left and not root.right:
        if root.value == sumv:
            res.append(root.value)
            print (res)
            return True
        else:
            return False

    if root.left and RootToLeaf(root.left,sumv-root.value,res):
        res.append(root.value)
        print (res)
        return True

    if root.right and RootToLeaf(root.right,sumv-root.value,res):
        res.append(root.value)
        print (res)
        return True
    return False

def maxSumPath(root):
    maxv = []
    maxv.append(-sys.maxint)
    calcSum(root,maxv)
    return maxv[0]

def calcSum(root,maxv):

    if not root:
        return 0

    left = calcSum(root.left,maxv)
    right = calcSum(root.right, maxv)

    current = max(root.value, max(root.value + left, root.value + right))
    maxv[0] = max(maxv[0], max(current, left + root.value + right))

    return current

x = Node(1500)
x.right = Node(1000)
x.left= Node(5)
x.right.right= Node(45)
x.right.left= Node(100)
x.left.right= Node(-20)
x.left.left= Node(-10)
x.left.left.right= Node(100)
x.right.right.left= Node(50)

# levelOrderPrint(x)

# print(RootToLeaf(x,2595))

print maxSumPath(x)