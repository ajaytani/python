class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None



def inOrder(head):
    if not head:
        return

    else:
        inOrder(head.left)
        print(head.value)
        inOrder(head.right)

def preOrder(head):
    if not head:
        return

    else:
        print(head.value)
        preOrder(head.left)
        preOrder(head.right)

def postOrder(head):
    if not head:
        return

    else:
        postOrder(head.left)
        postOrder(head.right)
        print(head.value)




