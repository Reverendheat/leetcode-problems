from typing import List

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]


s = Solution()
print(s.removeDuplicates(nums))
