from typing import List

digits = [1, 2, 3]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ints = [str(int) for int in digits]
        s_ints = "".join(ints)
        full_ints = int(s_ints)
        ints_plus_one = full_ints + 1
        str_ints = str(ints_plus_one)
        return [int(s) for s in str_ints]


s = Solution()
print(s.plusOne(digits))
