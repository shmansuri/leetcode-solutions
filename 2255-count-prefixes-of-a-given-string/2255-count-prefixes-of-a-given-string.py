class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        count = 0
        # for i in words:
        #     if s.startswith(i):
        #         count +=1
        
        # return count

        # without startswith method

        for word in words:
            if len(word) <= len(s):
                if word == s[:len(word)]:
                    count += 1
        
        return count
        