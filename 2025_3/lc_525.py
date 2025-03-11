class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        max_len = 0
        dict = {0:-1} #prefix: index
        #해당 누적합이 처음 나온 인덱스

        for i, k in enumerate(nums):
            if k == 0:
                prefix += -1
            if k == 1:
                prefix += 1
            print(prefix)

            if prefix in dict:
                #누적합이 같은 구간의 길이가 최대 길이
                max_len = max(max_len, i - dict[prefix])
            else:
                dict[prefix] = i


        return max_len
