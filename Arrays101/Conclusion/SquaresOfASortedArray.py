"""

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""

from typing import List

test_cases = [
    {"input": [-4, -1, 0, 3, 10], "output": [0, 1, 9, 16, 100]},
    {"input": [-7, -3, 2, 3, 11], "output": [4, 9, 9, 49, 121]},
]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nl = []
        for i in nums:
            nl.append(i * i)
        return sorted(nl)
