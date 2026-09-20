#1864. Minimum Number of Swaps to Make the Binary String Alternating

from typing import Counter

class Solution:
    def createAlternating(self, length: int) -> tuple[str, str]:
        res1 = ""
        res2 = ""
        for i in range(length):
            if i % 2 == 0:
                res1 += '0'
                res2 += '1'
            else:
                res1 += '1'
                res2 += '0'
        return (res1, res2)

    def minSwaps(self, s: str) -> int:
        cnt = Counter(s)

        diff = cnt['0'] - cnt['1']
        
        if abs(diff) > 1:
            return -1

        c0, c1 = self.createAlternating(len(s))
        
        swaps0 = 0
        swaps1 = 0

        for i in range(len(s)):
           if s[i] != c0[i]:
               swaps0 += 1
           if s[i] != c1[i]:
               swaps1 += 1
        
        if diff == 1:
            return swaps0//2
        elif diff == -1:
            return swaps1//2

        return min(swaps0//2, swaps1//2)



