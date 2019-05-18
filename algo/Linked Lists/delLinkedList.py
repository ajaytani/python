class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def LinkedList(head):

    def __init__(self,head):
        self.head = head

    def delNode(self, value):

        tmp = self.head
        prev =None

        if not tmp:
            raise ValueError("Data not in list")
        elif not tmp.next:
            if tmp.value != value:
                raise ValueError("Data not in list")
            elif tmp.value == value:
                return

        while tmp.next and tmp.value != value:
            prev = tmp
            tmp = tmp.next

        if not tmp.next:
            prev.next = None

        if tmp.next:
            prev.next = tmp.next

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False and current.value != data:
            if current.value == data:
                found = True
            else:
                previous, current = current, current.next
        if current is None:
            raise ValueError("Data not in list")
        if current.value == data:
            if previous is None:
                self.head = current.next
            elif previous is not None:
                previous.set_next(current.next)




