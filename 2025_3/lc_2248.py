class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        #모든 배열에 존재하는 정수
        dict = {}
        ans = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] not in dict:
                    dict[nums[i][j]] = 1
                else:
                    dict[nums[i][j]] += 1

        for key in dict:
            if dict[key] == len(nums):
                ans.append(key)
        ans.sort()
        return ans