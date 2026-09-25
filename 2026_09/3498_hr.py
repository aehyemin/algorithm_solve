class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        print(ord('z'))
        for i in range(len(s)):
            tmp = (ord('z') - ord(s[i]) + 1) *(i+1)
            print(tmp)
            ans += tmp
        return ans

            
        
