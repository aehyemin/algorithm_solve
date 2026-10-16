class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        #answer = [ [1에만 있는 요소], [2에만 있는 요소] ]
        one = set(nums1) - set(nums2)

        two = set(nums2) - set(nums1)
        return [list(one), list(two)]
