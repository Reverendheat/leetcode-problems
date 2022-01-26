from typing import List

nums = [12, 345, 2, 6, 7896]


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nums = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                even_nums += 1
        return even_nums


s = Solution()
print(s.findNumbers(nums))
