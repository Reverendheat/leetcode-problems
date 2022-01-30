"""

Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] 
that do not appear in nums.

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

"""

from typing import List

test_cases = [
    {"input": [4, 3, 2, 7, 8, 2, 3, 1], "output": [5, 6]},
    {"input": [1, 1], "output": [2]},
]


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers_set = set(range(1, len(nums) + 1))
        for num in nums:
            if num in numbers_set:
                numbers_set.remove(num)
        return list(numbers_set)


s = Solution()
for t in test_cases:
    try:
        if s.findDisappearedNumbers(t["input"]) != t["output"]:
            print(f"{t['input']} failed")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
