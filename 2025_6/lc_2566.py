class Solution:
    def minMaxDifference(self, num: int) -> int:
        #최대 숫자는 맨앞이 9가 아니면 9로 
        #최소 숫자는 맨앞이 0이 아니면 0으로
        num_str = str(num)
        num_str2 = str(num)
        key = 0
        key2 = 0
        big = []
        small = []
        #첫번째 숫자가 9인지 체크, 아니면 그 다음숫자 체크
        for i in num_str:
            if i != "9":
                key = i
                break

        #최댓값 만들기
        for i in num_str:
            if i != "9":
                tmp = i.replace(key, "9")
                big.append(tmp)
            else:
                big.append(i)



        #첫번째 숫자가 0인지 체크, 아니면 그 다음숫자
        for i in num_str2:
            if i != "0":
                key2 = i
                break

        #최솟값 만들기
        for i in num_str2:
            if i != "0":
                tmp = i.replace(key2, "0")
                small.append(tmp)
            else:
                small.append(i)


        big_val = int("".join(big))
        small_val = int("".join(small))
        return big_val - small_val

       