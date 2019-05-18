class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def maxHeapCheck(head):
    if not head or (not head.left and not head.right):
        return True

    else:
        check = False
        if head.left and head.value > head.left.value:
            check = True
        if head.right and head.value > head.right.value:
            check = True
        else:
            check = False
        return check

    return maxHeapCheck(head.left) and maxHeapCheck(head.right)


# x = Node(8)
# y = Node(3)
# z = Node(1)
# a = Node(6)
# b = Node(10)
# c = Node(9)
# d = Node(13)

x = Node(80)
y = Node(30)
z = Node(1)
a = Node(6)
b = Node(40)
c = Node(14)
d = Node(13)


x.left = y
y.left = z
y.right = a
x.right = b
b.right = c
c.left = d

print(maxHeapCheck(x))
