#accepted
# 
from typing import Counter


class Solution:
    def backtrack(self, counter, candidates, target, idx, l, res):
        if target == 0:
            res.append(l.copy())
            return
        if target < 0:
            return

        for i in range(idx, len(candidates)):
            if counter[candidates[i]] > 0:
                l.append(candidates[i])
                counter[candidates[i]] -= 1

                self.backtrack(counter, candidates, target - candidates[i], i, l, res)

                l.pop(-1)
                counter[candidates[i]] += 1

        return

    def combinationSum2(self, candidates, target):
        counter = Counter(candidates)
        candidates = sorted(counter.keys())
        print(counter)

        res = []
        l = []

        self.backtrack(counter, candidates, target, 0, l, res)

        return res


sol = Solution()

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

print(sol.combinationSum2(candidates, target))