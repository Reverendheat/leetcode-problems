"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Constraints
1 <= s.length <= 1000
s consists of lowercase English letters.

"""

input = ["a", "a", "a"]


class Solution:
    def countSubstrings(self, s: str) -> int:
        results = 0
        for i in range(0, len(s)):
            l = r = i
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    results += 1
                else:
                    break
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                    results += 1
                else:
                    break
        return results


s = Solution()
output = s.countSubstrings(input)
print(output)
