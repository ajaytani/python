class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def hasRight(self):
        return self.right

    def hasLeft(self):
        return self.left
#We can do this in one walk from top to bottom of our BST. This means O(h)O(h) time (again, that's O(\lg{n})O(lgn) if the tree is balanced, O(n)O(n) otherwise).
def secondHighest(head):
    parent = None
    currentNode = head
    while currentNode.hasRight():
        parent = currentNode
        currentNode = currentNode.right

    if currentNode.hasLeft:
        return currentNode.left

    else:
        return parent







class traversal:
    def __init__(self):
        self.headList = []


    def inOrderTraversal(self,head):
        while head:
            self.inOrderTraversal(head.left)
            self.headList.append(head)
            self.inOrderTraversal(head.right)





