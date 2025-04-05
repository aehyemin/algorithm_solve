from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #문자 위치 바꾸기
        #문자 통째로 바꾸기
        len1 = len(word1)
        len2 = len(word2)

        if len1 != len2:
            return False

        if set(word1) != set(word2):
            return False

        word1_c = sorted(Counter(word1).values())
        word2_c = sorted(Counter(word2).values())

        return word1_c == word2_c 