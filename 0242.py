#242. Valid Anagram

from collections import Counter

# Old solution return sorted(s) == sorted(t) which is O(2nlogn) instead of (2n) now.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        return Counter(s) == Counter(t)

