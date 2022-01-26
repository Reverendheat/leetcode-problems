from typing import List

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        for i in range(len(nums2) - 1, -1, -1):
            if nums2[i] in nums1:
                nums1.insert(i, nums2[i])
            else:
                nums1.append(nums2[i])
        nums1.sort()


s = Solution()
s.merge(nums1, m, nums2, n)
print(nums1)
