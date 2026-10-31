class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sep = s.split()
        n = len(sep)-1
        lastWord = sep[n]
        count = 0
        for i in lastWord:
            count += 1
        return count
        