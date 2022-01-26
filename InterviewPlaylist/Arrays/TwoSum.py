from typing import List

nums = [3, 2, 4]
target = 6

"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would 
have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     hm = self._get_hash_table(nums)
    #     for i, v in enumerate(nums):
    #         n = target - nums[i]
    #         if n in hm and i != hm[n]:
    #             return [i, hm[n]]

    # def _get_hash_table(self, nums: List[int]) -> dict[int, int]:
    #     hm = {}
    #     for i, v in enumerate(nums):
    #         hm[v] = i
    #     return hm

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, _ in enumerate(nums):
            n = target - nums[i]
            if n in nums and i != nums.index(n):
                return [i, nums.index(n)]


s = Solution()
print(s.twoSum(nums, target))
