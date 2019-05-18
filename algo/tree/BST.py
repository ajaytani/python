class Node:
    def __init__(self,key):
        self.left =None
        self.right = None
        self.value = key

def bst(treelst):
    if not treelst:
        return
    for i in xrange(len(treelst)-2):
        currentnode = Node()
        currentnode.value = treelst[i]
        if treelst[1+1] > treelst[i+2]:
            currentnode.left = Node(i+2)
            currentnode.right = Node(i+1)
        else:
            currentnode.right = Node(i + 2)
            currentnode.left = Node(i + 1)

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class BST( object ):
    def __init__( self ):
        self.root = None
    def getRoot( self ):
        return self.root
    def toCircularDoublyLinkedList_recursive( self ):
        head, tail = [None], [None]
        self._toCircularDoublyLinkedList_recursive( self.root, head, tail )
        if head[0] is not None:
            tail[0].right = head[0]
            head[0].left = tail[0]
        return head[0]
    def _toCircularDoublyLinkedList_recursive( self, n, h, t ):
        if n is None:
            return
# left
        if n.left is not None:
            self._toCircularDoublyLinkedList_recursive( n.left, h, t )

# visit
        if h[0] is None:
            h[0] = t[0] = n
        else:
            t[0].right = n # link right
            n.left = t[0] # link left
            t[0] = t[0].right # reassign tail
        self._toCircularDoublyLinkedList_recursive( n.right, h, t )