"""Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

"""


test_cases = [
  {
    "s":"badc",
    "t":"baba",
    "return": False
  },
  {
    "s":"egg",
    "t":"add",
    "return": True
  },
  {
    "s":"zeeb",
    "t":"zoob",
    "return": True
  },  
  {
    "s":"wada",
    "t":"eezz",
    "return": False
  },
  {
    "s":"foo",
    "t":"bar",
    "return": False
  },
]

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
      char_map = {}
      i = 0
      while i < len(s):
        if s[i] not in char_map.keys() and t[i] not in char_map.values():
          char_map[s[i]] = t[i]
        if char_map.get(s[i]) != t[i]:
          return False
        i += 1
      return True


def run_test_cases():
  s = Solution()
  for test in test_cases:
    res = s.isIsomorphic(test['s'],test['t'])
    assert res == test['return'], f"{res} incorrect for {test['s']}, should have returned {test['return']}"
  print("All tests passed!")


run_test_cases()