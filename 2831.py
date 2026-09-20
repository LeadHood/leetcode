#2831. Find the Longest Equal Subarray
# I did it but not really that optimized

class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        indexes: dict[int, list[int]] = {}
        
        for i in range(len(nums)):
            if nums[i] not in indexes:
                indexes[nums[i]] = []
            indexes[nums[i]].append(i)

        print(indexes)

        biggestSizeGap = 1
       
       #[1,2,1], k = 0
        for num, lis in indexes.items():
            left = 0

            for right in range(len(lis)):
                if left > right: 
                    continue

                numsGap = lis[right] - lis[left] + 1

                if numsGap - (right - left + 1) <= k:
                    biggestSizeGap = max(biggestSizeGap, right - left + 1)
                else:
                    left += 1

        return biggestSizeGap
