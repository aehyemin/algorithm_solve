class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #첫번째 방법 모든 인덱스를 저장하기
        #값: 값이 등장하는 인덱스
        #매칭되는 값 없으면 -1

        cardP = {}
        min_len = 1000000
        for i,k in enumerate(cards):
            if k not in cardP:
                cardP[k] = [i]
            else:
                cardP[k].append(i)
        for card, j in cardP.items():
            if len(j) >= 2:
                for i in range(1, len(j)):
                    leng = j[i] - j[i-1] + 1
                    min_len = min(min_len, leng)

        if min_len == 1000000:
            return -1
        else:
            return min_len