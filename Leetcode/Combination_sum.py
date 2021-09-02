# accepted
#
class Solution:
    def dfs(self, candidates, target, idx, l, res):
        if target < 0:
            return

        if not target:
            res.append(l.copy())
            return

        for i in range(idx, len(candidates)):
            l.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, l, res)
            l.pop(-1)

        return

    def combinationSum(self, candidates, target):
        candidates.sort()

        res = list()
        l = list()
        i = 0
        self.dfs(candidates, target, i, l, res)

        return res


sol = Solution()
candidates = [2, 3, 5]
target = 8

print(sol.combinationSum(candidates, target))