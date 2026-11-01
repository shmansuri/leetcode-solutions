class Solution:
    def addDigits(self, num: int) -> int:
        #Broute force
        # while num > 9:
        #     list1=[]
        #     while num > 0 :
        #         list1.append(num%10)
        #         num //= 10
        #     num = sum(list1)      
        # return num
        
    #optimal to previous
        # while num > 9:
        #     total = 0
        #     while num > 0:
        #         total += num % 10
        #         num //= 10
        #     num = total   
        # return num

        #most optimal code
        #time complexity = O(1)
        # space complexity = O(1)
        if num == 0:
            return 0
        
        return 1+ (num-1)%9
        
        
        