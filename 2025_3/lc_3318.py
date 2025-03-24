from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        #배열에서 요소 발생 횟수 카운트
        #top x 만큼 발생하는 것만. 둘이 같은 빈도면 더 큰 값 선택
        #결과 배열의 sum 계산
        #x만큼 구별된 요소 없으면 xsum 은 배열의 전체합
        num = Counter(nums[:k])
        sorted_num = sorted(num.items(), key=lambda x: (-x[1], -x[0]))
        ans =[]
        ans.append(sum(num * cnt for num, cnt in sorted_num[:x]))

        for i in range(k, len(nums)):
            old = nums[i-k]
            new = nums[i] 

            if old in num:
                num[old] -= 1
                if num[old] == 0:
                    del num[old]
            num[new] += 1

          
            sorted_num = sorted(num.items(), key=lambda x: (-x[1], -x[0]))

            ans.append(sum(num * cnt for num, cnt in sorted_num[:x]))

        return ans