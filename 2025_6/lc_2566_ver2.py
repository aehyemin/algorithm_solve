class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_l = str(num)

        for i in num_l:
            if i != "9":
                max_num = num_l.replace(i,"9")
                print(max_num)
                break
            else:
                max_num = num_l
        
        min_num = num_l.replace(num_l[0], "0")
        print(max_num, min_num)

        return int(max_num) - int(min_num)
