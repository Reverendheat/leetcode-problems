from typing import List

"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares 
of each number sorted in non-decreasing order.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

"""

nums = [-7, -3, 2, 3, 11]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nl = []
        for i in nums:
            nl.append(i * i)
        return sorted(nl)


s = Solution()
print(s.sortedSquares(nums))
