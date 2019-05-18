from __future__ import print_function
class Node(object):

    def __init__(self,value=0):
        self.next = None
        self.value = value

def reverse(head):
	if not head:
         return
	reverse(head.next)
	print(head.value, end=' ')

def reverseIter(head):
    Nodelist = []
    while head:
        Nodelist.append(head.value)
        head = head.next
    while Nodelist:
        print(Nodelist.pop(), end=' ')








x = Node(1)
y = Node(2)
z = Node(3)
x.next = y
y.next = z

reverse(x)
reverseIter(x)
reverseList(x)