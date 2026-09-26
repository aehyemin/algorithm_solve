class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        #리스트를 왼쪽부터 보면서 0이 아닌 숫자의 순서는 유지해야함
        #지금 보고 있는 위치, 어디 앞쪽에 두어야 하는지
        zero_spot = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i], nums[zero_spot] = nums[zero_spot], nums[i]
            zero_spot += 1
