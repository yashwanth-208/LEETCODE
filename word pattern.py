class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pToStr = {}
        strToP = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for pChar, word in zip(pattern, words):
            # Check if there's a conflict in the mapping from pattern to word
            if pChar in pToStr and pToStr[pChar] != word:
                return False
            # Check if there's a conflict in the mapping from word to pattern
            if word in strToP and strToP[word] != pChar:
                return False
            pToStr[pChar] = word
            strToP[word] = pChar
        return True