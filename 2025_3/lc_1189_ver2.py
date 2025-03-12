from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #balloon 텍스트가 몇번 들어가 있는지
        counts = Counter(text)

        b_cnt = counts['b']
        a_cnt = counts['a']
        l_cnt = counts['l'] // 2
        o_cnt = counts['o'] // 2
        n_cnt = counts['n']

        return min(b_cnt,a_cnt,l_cnt,o_cnt,n_cnt)