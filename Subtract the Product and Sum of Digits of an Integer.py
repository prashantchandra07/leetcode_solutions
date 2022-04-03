class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = []
        num = n
        while num > 0:
            cnst = num%10
            lst.append(int(cnst))
            num = int(num/10)
            
        prod = 1
        sum = 0
        
        for i in lst:
            prod = prod*i
            sum = sum+i
            
        diff = prod-sum
        
        return(diff)
        