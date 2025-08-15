

class Solution:
    def maxElement(self,nums):
        max=nums[0]
        secondmax=-1
        thirdmax=-1
        for i in nums:
            if i>max:
                thirdmax=secondmax
                secondmax=max
                max=i
            elif i>secondmax and i<max:
                thirdmax=secondmax
                secondmax=i
            elif i>thirdmax and i<secondmax:
                thirdmax=i
        return thirdmax
sk=Solution()

print("max element:",sk.maxElement([1,2,20,3,4,30,87,99,5,100]))



