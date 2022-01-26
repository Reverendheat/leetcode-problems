from typing import List

nums = [-7, -3, 2, 3, 11]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nl = []
        for i in nums:
            nl.append(i * i)
        return sorted(nl)


s = Solution()
print(s.sortedSquares(nums))
