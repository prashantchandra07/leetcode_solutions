#   Questions:  https://leetcode.com/problems/count-integers-with-even-digit-sum/

class Solution:
    def countEven(self, num: int) -> int:
        lst = []
        while num > 0:
            var_s = num
            var_t = 0
            while var_s > 0 :
                var_u = var_s%10
                var_t = int(var_t+var_u)
                var_s = var_s/10
            if var_t%2 == 0:
                lst.append(num)
            num = num-1
        
        return(len(lst))
