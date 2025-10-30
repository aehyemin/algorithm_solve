def solution(nums):
    n = len(nums) // 2
    sets = set(nums)

    if len(sets) >= n:
        return n
    else:
        return len(sets)
