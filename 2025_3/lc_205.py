class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # replace 를 사용해야 할것같다 => 실패
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False

        l_s = list(s)
        l_t = list(t)

        print(l_s, l_t)

        for i in range(s_len):
            l_t[i]=s[i]
        for j in range(t_len):
            l_s[j]= t[j] 
        print(l_s, l_t)

        return "".join(l_s) == t and "".join(l_t) == s 