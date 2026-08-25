class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        l=len(set(sentence))
        if l==26:
            return True
        else:
            return False
        