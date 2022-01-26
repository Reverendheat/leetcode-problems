from typing import List

"""

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

"""

test_cases = [
    {"input": [3, 1, 2, 4], "output": [2, 4, 3, 1]},
    {"input": [1, 1, 2, 2], "output": [2, 2, 1, 1]},
    {"input": [0, 5], "output": [0, 5]},
    {"input": [1, 2, 3, 4, 5, 6, 7, 8], "output": [8, 6, 4, 2, 7, 5, 3, 1]},
]


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] % 2 != 0:
                nums.append(nums.pop(i))
            i += 1
        print(nums)
        return nums


s = Solution()
for t in test_cases:
    try:
        if s.sortArrayByParity(t["input"]) != t["output"]:
            print(f"{t['input']} failed")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
