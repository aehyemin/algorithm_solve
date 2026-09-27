class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        i=0
        if len(word1) < len(word2):
            short = len(word1)
        else:
            short = len(word2)
        while i < short:
            new += word1[i]
            new += word2[i]
            i+=1
        #하나씩 번갈아 가면서 추가한다
        #하나 짧은게 먼저 끝날경우, 나머지는 뒤에 다 추가한다.
        if len(word1) == short:
            new += word2[short:]
        else:
            new += word1[short:]
        return new





               
        
