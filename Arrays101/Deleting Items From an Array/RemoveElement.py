from typing import List

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] != val:
                nums.insert(0, nums.pop(i))
                k += 1
            i += 1
        return k


s = Solution()
print(s.removeElement(nums, val))
