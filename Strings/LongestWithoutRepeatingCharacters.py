"""
Given a string s, find the length of the longest substring without repeating characters.

Constraints
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

input = "bpfbhmip "

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = ""
        substrings = []
        i = 0
        while i < len(s):
            if s[i] not in current_substring:
                current_substring += s[i]
            else:
                substrings.append(current_substring)
                last_known = current_substring
                current_substring = ""
                valid_chars_reversed = ""
                for j in range(len(last_known) - 1, -1, -1):
                    if last_known[j] != s[i]:
                        valid_chars_reversed += last_known[j]
                    else:
                        break
                current_substring = "".join([valid_chars_reversed[b] for b in range(len(valid_chars_reversed) -1,-1,-1)]) + s[i]
            i += 1
        substrings.append(current_substring)
        longest_string = ""
        for i in substrings:
            if len(i) > len(longest_string):
                longest_string = i
        return len(longest_string)

s = Solution()
a = s.lengthOfLongestSubstring(input)

assert a == 7, ""