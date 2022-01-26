from typing import List

nums = [12, 345, 2, 6, 7896]

"""

Given an array nums of integers, return 
how many of them contain an even number of digits.

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105

"""


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nums = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even_nums += 1
        return even_nums


s = Solution()
print(s.findNumbers(nums))
