from collections import defaultdict
from typing import List

"""
  Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

  After doing so, return the array.

  Constraints:

  1 <= arr.length <= 104
  1 <= arr[i] <= 105
"""

test_cases = [
    {"input": [400], "output": [-1]},
    {"input": [17, 18, 5, 4, 6, 1], "output": [18, 6, 6, 6, 1, -1]},
]


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = arr[len(arr) - 1]
        arr[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            current_val = arr[i]
            arr[i] = max_right
            if max_right < current_val:
                max_right = current_val
        return arr


s = Solution()
for t in test_cases:
    try:
        if s.replaceElements(t["input"]) != t["output"]:
            print(f"{t['input']} failed!")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
