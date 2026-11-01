class Solution:
    def minimumSum(self, num: int) -> int:
        list1=[]
        while num>0:
            list1.append(num%10)
            num //= 10
        list1.sort()
        new1 = (list1[0]*10)+ list1[2]
        new2 = (list1[1]*10) + list1[3]
        return new1+new2

        