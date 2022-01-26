from typing import List

arr = [1, 0, 2, 3, 0, 4, 5, 0]


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]
                    print(arr)


s = Solution()
s.duplicateZeros(arr)
print(arr)
