def insert(intervals, new_interval):
    if new_interval[1] < new_interval[0]:
        new_interval = (new_interval[1], new_interval[0])
    n = len(intervals)
    if new_interval[0] > intervals[n - 1][1]:
        intervals.append(new_interval)
        return intervals
    if new_interval[1] < intervals[0][0]:
        return [new_interval] + intervals
    start = 0
    end = -1
    for i in range(n):
        if new_interval[0] > intervals[i][0] or new_interval[0] > intervals[i][1]:
            start = i
        if new_interval[1] < intervals[i][0] or new_interval[1] < intervals[i][1]:
            if end == -1:
                end = i

    lst = []
    i = 0
    if n > end - start:
        while i < n - (end - start):
            if i < start:
                lst.append(intervals[i][0])
            elif i > end:
                lst.append(intervals[i][0])
            elif i == start:
                if intervals[i][0] > new_interval[0]:
                    x = new_interval[0]
                else:
                    x = intervals[i][0]
            elif i == end:
                if intervals[i][1] > new_interval[0] and intervals[i][1] < new_interval[1]:
                    y = new_interval[0]
                if new_interval[1] <= intervals[i][1]:
                    y = intervals[i][1]
            lst.append((x, y))
    return lst

A =[(1,2),(4,6)]
B = (10,8)

print(insert(A,B))