class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #하나의 알파벳이 하나의 단어를 매핑
        s_l = s.split(" ")
        hash = {}

        if len(s_l) != len(pattern):
            return False

        for i in range(len(s_l)):
            alpha = pattern[i]
            word = s_l[i]
        
            if alpha not in hash:
                if word not in hash.values():
                    hash[alpha] = word
                else:
                    return False
            else:
                if hash[alpha] != word:
                    return False
        return True 