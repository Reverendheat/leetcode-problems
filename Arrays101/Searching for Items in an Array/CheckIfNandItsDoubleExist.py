from typing import List

arr = [10, 2, 5, 3]

"""

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

"""


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
