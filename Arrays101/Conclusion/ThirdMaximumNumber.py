"""

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

"""

from typing import List


test_cases = [
    {"input": [1, 2], "output": 2},
    {"input": [1, 1, 2], "output": 2},
    {
        "input": [3, 2, 1],
        "output": 1,
    },
    {
        "input": [2, 2, 3, 1],
        "output": 1,
    },
    {
        "input": [14],
        "output": 14,
    },
    {
        "input": [2, 2, 2, 2, 1],
        "output": 2,
    },
]


class Solution:
    def _remove_duplicates(self, sorted_nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(sorted_nums):
            if sorted_nums[i] == sorted_nums[j]:
                sorted_nums.pop(j)
            else:
                i += 1
                j += 1
        return sorted_nums

    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        else:
            sn = sorted(nums)
            rd = self._remove_duplicates(sn)
        return rd[-3] if len(rd) > 2 else rd[-1]


s = Solution()
for t in test_cases:
    try:
        if s.thirdMax(t["input"]) != t["output"]:
            print(f"{t['input']} failed")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
