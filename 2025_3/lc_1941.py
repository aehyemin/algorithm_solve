class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #모든 문자가 같은 빈도로 출현하면 good 
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
     
        first = list(dict.values())[0]

        while dict:
            for key in dict:
                if dict[key] != first:
                    return False
            return True