class Node(object):
    def __init__(self, next = None, value = None):
        self.next = next
        self.value = 0

    def get_data(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next = new_next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self,data):
        current = self.head
        previous = None
        found = False
        while current and found is False and current.get_data() != data:
            if current.get_data() == data:
                found = True
            else:
                previous, current = current, current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if current.get_data() == data:
            if previous is None:
                self.head = current.get_next()
            elif previous is not None:
                previous.set_next(current.get_next())

    def deldups(self):
        current = self.head
        while current:
            runner = current
            while runner.next is not None:
                if runner.next.get_data() == current.get_data():
                    runner.next = runner.next.get_next()
                else:
                    runner = runner.get_next()
            current = current.get_next()

    def kthelementtolast(self):
        target = self.head
        last = self.head
        for i in range(k):
            if last is None:
                return last
            last = last.next
        while last is not None:
            target = target.next
            last = last.next
        return target

    # def partition(head,x):
    #     realhead = head
    #     iter = head
    #     while iter is not None and iter.next is not None:
    #         if iter.next.data < x:
    #             temp = iter.next
    #             iter.next = temp.next
    #             temp.next = realhead
    #             realhead = temp
    #         iter = iter.next
    #     return realhead

    def partition(self, node, x):
        head = node
        tail = node
        while node is not None:
            next = node.next
            if node.get_data() < x:
                node.next = head
                head = node
            else:
                tail.next = node
                tail = node
            node = next
        tail.next = None
        return head





