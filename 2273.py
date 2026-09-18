#2273. Find Resultant Array After Removing Anagrams

class Solution:
    # Strings have to be sorted
    def areAnagrams(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False

        for x, y in zip(a, b):
            if x != y:
                return False

        return True

    def removeAnagrams(self, words: list[str]) -> list[str]:
        newWords = [''.join(sorted(word)) for word in words]
        
        i = len(words) - 1

        while i >= 1:
            if Solution.areAnagrams(self, newWords[i], newWords[i - 1]):
                words.pop(i)

            i -= 1


        return words
