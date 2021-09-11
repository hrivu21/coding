# accepted
#
#
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        import random

        def quicksort(arr, start, stop):
            if start < stop:
                pivotindex = partitionrand(arr, start, stop)
                quicksort(arr, start, pivotindex - 1)
                quicksort(arr, pivotindex + 1, stop)

        def partitionrand(arr, start, stop):

            randpivot = random.randrange(start, stop)

            arr[start], arr[randpivot] = arr[randpivot], arr[start]
            return partition(arr, start, stop)

        def partition(arr, start, stop):
            pivot = start  # pivot
            i = start + 1  # a variable to memorize where the
            # partition in the array starts from.
            for j in range(start + 1, stop + 1):
                if arr[j] <= arr[pivot]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i + 1
            arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
            pivot = i - 1
            return pivot

        if len(nums) == 1:
            return

        currmax = nums[-1]
        currmaxidx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):

            if nums[i] < nums[i + 1]:
                justgreater = nums[i + 1]
                justgreateridx = i + 1

                for idx in range(i + 1, len(nums)):
                    if nums[i] < nums[idx] and nums[idx] < justgreater:
                        justgreater = nums[idx]
                        justgreateridx = idx
                nums[i], nums[justgreateridx] = nums[justgreateridx], nums[i]
                quicksort(nums, i + 1, len(nums) - 1)
                return

        nums.sort()


sol = Solution()
nums = [1, 3, 2]
sol.nextPermutation(nums)
print(nums)