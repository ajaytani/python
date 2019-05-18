class MinHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize =0
    def buildHeap(self,arr):
        self.currentSize = len(arr)
        self.heapList = [0] + arr
        i = self.currentSize//2
        while i > 0:
            self.percDown(i)
            i = i-1

    def percDown(self,i):
        while i*2 <self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] >self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def heapPop(self):
        self.currentSize -=1
        return self.heapList.pop()



    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        return self.heapList

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                 self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2],self.heapList[i]
            i =i // 2

    def delMin(self):
            retVal = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize -= 1
            self.heapList.pop()
            self.percdown(1)
            return retVal

def getMini(tasks,worker):
    tot = sum(tasks)
    #sort tasks
    tasks.sort(reverse=True) # put in the largest time first
    # the idea is to get as averaged as possible,
    # every iteration we add the smallest value to the currently smallest worker
    times = [0]*worker
    x= MinHeap()
    x.buildHeap(times)
    for i in tasks:
        t=x.heapPop()
        times = x.insert((t+i))
    return times

print(getMini([2,2,36,3,5,2,4,46,76,4,23,12,41,63,34,1,13,7,3,21,4,7,1],5))



import heapq
def getMini2(tasks,worker):
    tot = sum(tasks)
    tasks.sort(reverse=True) # put in the largest time first
    times = [0]*worker
    heapq.heapify(times)
    for i in tasks:
        t=heapq.heappop(times)
        heapq.heappush(times,(t+i))
    return max(times)

print(getMini2([2,2,36,3,5,2,4,46,76,4,23,12,41,63,34,1,13,7,3,21,4,7,1],5))


def find_loc(scheduler, task):
    w_times = []
    for wrkr in scheduler:
        w_times.append(sum(wrkr))
    max_time = max(w_times)
    avail_time = 0
    loc = 0
    for i in range(len(scheduler)):
        if max_time - w_times[i] > avail_time:
            avail_time = max_time - w_times[i]
            loc = i
    return loc


def get_min_time(a, n):
    a.sort(reverse=True)
    print a
    scheduler = [[] for i in range(n)]
    scheduler[0].append(a[0])

    i = 1
    while i < len(a):
        loc = find_loc(scheduler, a[i])
        scheduler[loc].append(a[i])
        i += 1

    return scheduler


if __name__ == '__main__':
    scheduler = get_min_time([2, 2, 3, 7, 1], 3)
    print (scheduler)

