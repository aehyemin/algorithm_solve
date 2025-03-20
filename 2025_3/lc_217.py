class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #두번이상 나타난 값이 있으면 true
        has = {}
        for i in nums:
            if i not in has:
                has[i] = 1
            else:
                return True
        return False
        