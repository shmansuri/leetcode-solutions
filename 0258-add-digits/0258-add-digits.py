class Solution:
    def addDigits(self, num: int) -> int:
        #Broute force
        while num > 9:
            list1=[]
            while num > 0 :
                list1.append(num%10)
                num //= 10
            num = sum(list1)
        
        return num
        
        
        
        
        