


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        for i in range(0, len(nums), 1):
            if nums[i] >= target:
                return i
            if i == len(nums) - 1 and nums[i] > target:
                return i
            elif i == len(nums) - 1 and nums[i] < target:
                return i + 1


nums = [1,3,5,6]
target = 7
solution = Solution()
print(solution.searchInsert(nums, target))