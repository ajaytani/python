class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        def aux(ans, cur, A, B):
            if sum(cur) > B:
                return
            elif sum(cur) == B:
                if cur not in ans:
                    ans.append(cur)
                return

            for i in A:
                aux(ans, sorted(cur + [i]), A, B)
            return

        A.sort()
        ans = []
        aux(ans, [], A, B)
        return ans


x =Solution()

x.combinationSum([10,15,55],85 )