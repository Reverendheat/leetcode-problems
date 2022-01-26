from typing import List

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        new_arr = [None] * len(nums)
        while i < len(nums):
            new_arr[(i + k) % len(nums)] = nums[i]
            i += 1
        for i in range(0, len(new_arr)):
            if new_arr[i] is None:
                continue
            nums[i] = new_arr[i]


s = Solution()
print(s.rotate(nums, k))
