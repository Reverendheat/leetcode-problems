from typing import List

"""

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

"""

test_cases = [
    {"input": [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 11], "output": True},
    {"input": [3, 5, 5], "output": False},
    {"input": [2, 0, 2], "output": False},
    {"input": [2, 0], "output": False},
    {"input": [2], "output": False},
    {"input": [], "output": False},
    {"input": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "output": False},
    {"input": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0], "output": False},
]


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        j = len(arr) - 1
        if len(arr) > 2:
            for _ in range(len(arr)):
                if i == len(arr) - 1 or j == 0:
                    return False
                if arr[i] < arr[i + 1]:
                    i += 1
                if arr[j] < arr[j - 1]:
                    j -= 1
            if i == j and i != 0 and j != len(arr) - 1:
                return True
            return False


s = Solution()
for t in test_cases:
    try:
        if s.validMountainArray(t["input"]) != t["output"]:
            print(f"{t['input']} failed!")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
