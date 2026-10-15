class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        s_l = list(s)
        cnt = 0
        window = s_l[:k]
        
        for j in window:
            if j in vowel:
                cnt += 1
        max_cnt = cnt 
        for i in range(k, len(s)):
            now = s[i]
            out = s[i-k]
            if now in vowel:
                cnt += 1
            if out in vowel:
                cnt -= 1
            if cnt > max_cnt:
                max_cnt = cnt
            
            
        return max_cnt
            
           
