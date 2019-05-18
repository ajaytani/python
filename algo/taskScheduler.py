def find_loc(scheduler):
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

    for i in range(1,len(a)):
        loc = find_loc(scheduler)
        scheduler[loc].append(a[i])

    return scheduler


if __name__ == '__main__':
    scheduler = get_min_time([2, 4, 4, 4 , 1], 3)
    print scheduler


    def laceStringsRecur(s1, s2):
        """
        s1 and s2 are strings.

        Returns a new str with elements of s1 and s2 interlaced,
        beginning with s1. If strings are not of same length,
        then the extra elements should appear at the end.
        """

        def helpLaceStrings(s1, s2, out):
            if s1 == '':
                return out + s2
            if s2 == '':
                return out + s1
            else:
                return helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])

        return helpLaceStrings(s1, s2, '')