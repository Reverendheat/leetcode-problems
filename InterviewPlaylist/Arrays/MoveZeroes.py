from typing import List

nums = [0, 1, 0, 3, 12]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.append(0)
                del nums[i]
        return nums


s = Solution()
print(s.moveZeroes(nums))