from typing import List

arr = [10, 2, 5, 3]


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            j = len(arr) - 1
            while j > -1:
                if arr[i] * 2 == arr[j] and j != i:
                    return True
                j -= 1
            i += 1
        return False


s = Solution()
print(s.checkIfExist(arr))
