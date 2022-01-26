from typing import List

"""

Given a binary array nums, return the maximum number 
of consecutive 1's in the array.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""

nums = [1, 1, 0, 1, 1, 1]


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_count = 0
        for i in nums:
            if i == 1:
                current_count += 1
            else:
                current_count = 0
            if current_count > max_consecutive:
                max_consecutive = current_count
        return max_consecutive


s = Solution()
print(s.findMaxConsecutiveOnes(nums))
