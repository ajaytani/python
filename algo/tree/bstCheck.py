#inorder traversal is always sorted for BST
import sys
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def bstCheck(head):
    trv = traversal()
    trv.inOrder(head)
    curr = -sys.maxsize
    for i in trv.headlist:
        if curr > i:
            return False
        else:
            curr = i
    return True


class traversal:
    def __init__(self):
        self.headlist = []

    def inOrder(self,head):
        if not head:
            return

        else:
            self.inOrder(head.left)
            self.headlist.append(head.value)
            self.inOrder(head.right)


x = Node(8)
y = Node(3)
z = Node(1)
a = Node(6)
b = Node(10)
c = Node(9)
d = Node(13)

x.left = y
y.left = z
y.right = a
x.right = b
b.right = c
c.left = d


print(bstCheck(x))


# minv = sys.maxsize
# maxv = -sys.maxsize
# print(bstCheck(x,minv,maxv))