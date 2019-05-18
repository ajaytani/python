class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        master = []
        self.recurse([x for x in range(1, n + 1)], k, master, 0, "")
        return master

    def recurse(self, S, have, master, curr, buff):
        if have == 0:
            master.append([int(x) for x in buff.split()])
        elif curr < len(S) and have > 0:
            self.recurse(S, have - 1, master, curr + 1, buff + " " + str(S[curr]))
            self.recurse(S, have, master, curr + 1, buff)

x = Solution()
print(x.combine(3,2))