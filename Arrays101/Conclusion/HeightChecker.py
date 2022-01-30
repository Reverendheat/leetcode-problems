"""

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height.
Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in.
Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

"""

from typing import List


test_cases = [
    {"input": [1, 2, 3, 4, 5], "output": 0},
    {
        "input": [5, 1, 2, 3, 4],
        "output": 5,
    },
]


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        i = 0
        output = 0
        while i < len(sorted_heights):
            if sorted_heights[i] != heights[i]:
                output += 1
            i += 1
        return output


s = Solution()
for t in test_cases:
    try:
        if s.heightChecker(t["input"]) != t["output"]:
            print(f"{t['input']} failed")
        else:
            print(f"{t['input']} passed!")
    except Exception as e:
        print(f"{t['input']} failed with exception {e}")
