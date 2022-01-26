from typing import List

nums = [1, 0, 1]

"""
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity 
and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i = 0
        while i < len(sorted_nums):
            if (
                sorted_nums[i] == sorted_nums[-1]
                or sorted_nums[i] != sorted_nums[i + 1]
            ):
                return sorted_nums[i]
            i += 2


s = Solution()
print(s.singleNumber(nums))
