class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        #모든 문자가 같은 빈도로 출현하면 good 
        dict = {}
        for char in s:
            dict[char] = dict.get(char,0) + 1

        return len(set(dict.values())) == 1 #boolean 값
