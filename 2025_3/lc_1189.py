class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #balloon 텍스트가 몇번 들어가 있는지
        
        b_cnt = text.count('b')
        a_cnt = text.count('a')
        l_cnt = text.count('l') // 2
        o_cnt = text.count('o') // 2
        n_cnt = text.count('n')

        return min(b_cnt, a_cnt, l_cnt, o_cnt, n_cnt)