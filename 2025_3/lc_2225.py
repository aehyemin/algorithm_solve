class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #answer[0] 경기에서 패하지 않은 플레이어
        #answer[1] 정확히 한번 패배한 플레이어
        #오름차순 출력
        #matches = [승자, 패자]
        dict = {} #패배 횟수를 저장
        cur = 0

        for winner, loser in matches:
            if winner not in dict:
                dict[winner] = 0

            if loser not in dict:
                dict[loser] = 1
            else:
                dict[loser] += 1

        win = []
        lose_one = []
        for player, lose in dict.items():
            if lose == 0:
                win.append(player)
            if lose == 1:
                lose_one.append(player)

        return [sorted(win), sorted(lose_one)]
