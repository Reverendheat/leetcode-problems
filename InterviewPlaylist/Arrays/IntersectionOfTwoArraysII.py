from typing import List

nums1 = [4, 5, 9]
nums2 = [4, 4, 8, 9, 9]

"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it
shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ol = self._order_lists_by_size(nums1, nums2)
        hmap_1 = self._return_hash_map(ol[1])
        output_arr = []
        for n in ol[0]:
            if n in hmap_1:
                if hmap_1[n] > 0:
                    output_arr.append(n)
                    hmap_1[n] -= 1
        return output_arr

    def _order_lists_by_size(self, l1, l2) -> tuple[list[int]]:
        return l1, l2 if len(l2) > len(l1) else l2, l1

    def _return_hash_map(self, nums: List[int]) -> dict[int, int]:
        hm = dict.fromkeys(nums, 0)
        for i in nums:
            hm[i] += 1
        return hm


s = Solution()

print(s.intersect(nums1, nums2))
