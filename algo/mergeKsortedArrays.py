import sys
# // Every Node will store the data and the list no from which it belongs
class HeapNode(object):
    def __init__(self, data, listNo):
        self._data = data
        self._listNo = listNo


class MergeKSortedArrays(object):
    def __init__(self, size):
        self.size = size
        self.Heap = HeapNode(size+1,-1)
        self.position = 0
        self.result = []

    def MergeKSortedArrays(self,k):
        self.size = k
        Heap = HeapNode(0,-1)
        position = 0
        Heap[0] = HeapNode(0, -1)

    def merge(self,A, k, n):
        nk = n * k
        result = []
        count = 0
        ptrs = []
        for i in range(k):
            ptrs.append(0)
        for i in range(k):
            if (ptrs[i] < n):
                self.insert(A[i][ptrs[i]], i)
            else:
                self.insert(sys.maxsize, i)

        while (count < nk):
            h = self.extractMin()  # get the min node from the heap.
            result[count] = h.data  # store node data into result array
            ptrs[h.listNo] += 1  # increase the particular list pointer
            if (ptrs[h.listNo] < n):  # check if list is not burns out
                self.insert(A[h.listNo][ptrs[h.listNo]], h.listNo)  # insert the next element from the list
            else:
                self.insert(sys.maxsize, h.listNo)  # if any of this list burns out, insert +infinity
                count += 1
        return result

    def insert(self,data, listNo):
        if (self.position == 0):  # check if Heap is empty
            self.Heap = HeapNode(data, self.position + 1)  # insert the first element in heap
            position = 2
        else:
            self.Heap[self.position + 1] = HeapNode(data, listNo)  # insert the element to the end
            self.bubbleUp()  # call the bubble up operation


    def extractMin(self):
        min = self.Heap[1]  # // extract the root
        self.Heap[1] = self.Heap[self.position - 1]  # // replace the root with the last element in the heap
        self.Heap[self.position - 1] = None  # // set the last Node as NULL
        self.position -= 1  # // reduce the position pointer
        self.sinkDown(1)  # // sink down the root to its correct position
        return min


    def sinkDown(self,k):
        smallest = k;
    #	// check which is smaller child , 2k or 2k+1.
        if (2 * k < self.position and self.Heap[smallest].data > self.Heap[2 * k].data):
            smallest = 2 * k
        if (2 * k + 1 < self.position and self.Heap[smallest].data > self.Heap[2 * k + 1].data):
            smallest = 2 * k + 1
        if (smallest != k):  # if any if the child is small, swap
            self.swap(k, smallest)
            self.sinkDown(smallest)  # // call recursively


    def swap(self,a, b):
    # // System.out.println("swappinh" + mH[a] + " and " + mH[b]);
        temp = self.Heap[a]
        self.Heap[a] = self.Heap[b]
        self.Heap[b] = temp


    def bubbleUp(self):
        pos = self.position - 1  # // last position
        while (pos > 0 and self.Heap[pos / 2].data > self.Heap[pos].data):  # // check if its parent is greater.
            y = self.Heap[pos]  # // if yes, then swap
            self.Heap[pos] = self.Heap[pos / 2]
            self.Heap[pos / 2] = y
            pos = pos / 2  # // make pos to its parent for next iteration.


A = [[] for i in range(5)]
A[0] = [1, 5, 8, 9]
A[1] = [2, 3, 7, 10]
A[2] = [4, 6, 11, 15]
A[3] = [9, 14, 16, 19]
A[4] = [2, 4, 6, 9]
m = MergeKSortedArrays(len(A))
m.size = len(A)
op = m.merge(A, len(A), len(A[0]))
print(op)


