from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #만약 s2가 s1의 순열을 포함하면 true
        #s2의 substring이 s1의 순열 중 하나이면 true
        len_s1 = len(s1)
        len_s2 = len(s2)
        
        if len_s1 > len_s2:
            return False
        
        s1_count = Counter(s1)
        window = Counter(s2[:len_s1])

        if s1_count == window:
            return True

        for i in range(len_s1, len_s2):
            a_char = s2[i-len_s1]
            new_char = s2[i]

            window[a_char] -= 1
            window[new_char] += 1

            if window[a_char] == 0:
                del window[a_char]

            if s1_count == window:
                return True
        return False
  