class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
# 모든 인덱스를 저장하지 않고, 각 숫자에 대해 마지막으로 등장한 인덱스만 저장
# 배열을 순회하면서, 현재 숫자가 이전에 등장한 적 있다면 현재 인덱스와 저장해둔 인덱스의 차이를 계산해 갱신
# 해당 숫자의 인덱스를 현재 인덱스로 저장
        dict = {}
        min_len = 1000000
        for idx, val in enumerate(cards):
            if val in dict:
                min_len = min(min_len, idx - dict[val] + 1)
                dict[val] = idx
            else:
                dict[val] = idx

        if min_len == 1000000:
            return -1
        else:
            return min_len