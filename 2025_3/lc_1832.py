class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict = {}
        for char in sentence:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        if len(dict) == 26:
            return True
        else:
            return False