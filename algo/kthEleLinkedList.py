class Node(object):

    def __init__(self,next = None, value = None):
        self.next = None
        self.value = 0

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next = new_next

    def __repr__(self):
        return 'LinkedList({}, {})'.format(self.value, repr(self.next))

class linkedList(object):

    def __init__(self, head = None):
        self.head = head

    # insert at head
    def insert(self,data):
        new_node = Node(data)
        new_node.value = data
        new_node.next = self.head
        self.head =  new_node

    def printList(self):
        temp = self.head
        while temp:
            print temp.value
            temp = temp.next

    def kthelementFromList(self,k):
        kthnode =  self.head
        lastnode = self.head

        for i in range(k):
            if lastnode is None:
                return lastnode
            lastnode = lastnode.next

        while lastnode:
            kthnode = kthnode.next
            lastnode = lastnode.next

        return kthnode

    def reverseRecursive(self):
        self._reverseRecursive(self.head)

    def _reverseRecursive(self, n):
        if n:
            right = n.next

            if self.head != n:
                n.next = self.head
                self.head = n
            else:
                n.next = None
            print "right : " , right
            self._reverseRecursive(right)


x = linkedList()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)
x.insert(6)
print x.printList()
x.reverseRecursive()

print x.printList()





