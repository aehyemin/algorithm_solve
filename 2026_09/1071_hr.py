class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #candies[i] = i번째 아이가 가진 캔디 수, entracandies=내가가진 여분의 캔디
        #i번째 아이에게 all extra를 줬을때, 그 아이가 최고면 true, 아니면 false.
        #를 모든 리스트를 돌았을때의 가정으로 [list true or false로]
        result = []
        max_one = max(candies)
        for i in range(len(candies)):
            #[2,3,5,1,3]
            if candies[i] + extraCandies >= max_one:
                result.append(True)
            else:
                result.append(False)
        return result




