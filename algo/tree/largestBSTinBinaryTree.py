"""
 * Video link - https://youtu.be/4fiDs7CCxkc
 * Given a binary tree, find size of largest binary search subtree in this
 * binary tree.

 * Traverse tree in post order fashion. Left and right nodes return 4 piece
 * of information to root which isBST, size of max BST, min and max in those
 * subtree. 
 * If both left and right subtree are BST and this node data is greater than max
 * of left and less than min of right then it returns to above level left size +
 * right size + 1 and new min will be min of left side and new max will be max of
 * right side.
 """
import sys
import collections

class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class ConstructTreeFromInOrderPreOrder:

    def __init__(self):
        self.index = 0

    def createTree1(self,inorder,preorder ):
        result =  self.createTree(inorder, preorder, 0, len(inorder)-1)
        self.index = 0
        return result

    def createTree(self, inorder, preorder, start, end):
        if start > end:
            return None
        for i in range(start,end+1):
            if preorder[self.index] == inorder[i]:
                break

        node = Node(preorder[self.index])
        self.index +=1
        node.left = self.createTree(inorder, preorder, start, i - 1)
        node.right = self.createTree(inorder, preorder, i + 1, end)
        return node

def levelOrderTree(root):

    if not root:
        return
    currentcount = 1
    nextcount = 0
    nodes = collections.deque([root])
    while len(nodes) != 0:

        currentnode = nodes.popleft()
        currentcount -= 1
        print currentnode.data,

        if currentnode.left:
            nodes.append(currentnode.left)
            nextcount += 1
        if currentnode.right:
            nodes.append(currentnode.right)
            nextcount += 1

        if currentcount == 0:
            print '\n'
            currentcount, nextcount = nextcount, currentcount



class MinMax:
    def __init__(self):
        self.min = -sys.maxsize
        self.max = sys.maxsize
        self.isBST = True
        self.size = 0

def trimBST(root,minVal,maxVal):

    if not root:
        return

    root.left = trimBST(root.left,minVal,maxVal)
    root.right = trimBST(root.right, minVal, maxVal)

    if minVal <= root.data <= maxVal:
        return root

    if root.data < minVal:
        return root.right

    if root.data > maxVal:
        return root.left

def checkBST(self,root):
    treeVal = []
    self.inorder(root)
    self.sortcheck(treeVal)

    def inorder(self,root):
        if not root:
            return
        inorder(root.left)
        treeVal.append(root.value)
        inorder(root.right)

    def sortcheck(self,treeVal):
        return treeVal == sorted(treeVal)






class LargestBSTInBinaryTree:

    def largestBST(self,root):
        m = self.largest(root)
        return m.size

    def largest(self,root):
        if not root:
            rm = MinMax()
            return rm
        leftMinMax = self.largest(root.left)
        rightMinMax = self.largest(root.right)

        m = MinMax()

        if not leftMinMax.isBST or not rightMinMax.isBST or (leftMinMax.max > root.data or rightMinMax.min <= root.data):
            m.isBST = False
            m.size = max(leftMinMax.size, rightMinMax.size)
            return m


        m.isBST = True
        m.size = leftMinMax.size + rightMinMax.size + 1

        m.min = leftMinMax.min if root.left else root.data
        m.max = rightMinMax.max if root.right else root.data

        return m

if __name__ == '__main__':
    lbi = LargestBSTInBinaryTree()
    ctf = ConstructTreeFromInOrderPreOrder()
    inorder = [-7, -6, -5, -4, -3, -2, 1, 2, 3, 16, 6, 10, 11, 12, 14]
    preorder = [3, -2, -3, -4, -5, -6, -7, 1, 2, 16, 10, 6, 12, 11, 14]
    root = ctf.createTree1(inorder, preorder)
    levelOrderTree(root)
    largestBSTSize = lbi.largestBST(root)
    print("Size of largest BST  is ", largestBSTSize)
    # assert largestBSTSize == 8
