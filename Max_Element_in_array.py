
class Solution:
    def maxElement(self,nums):
        max=nums[0]
        for i in nums:
            if i>max:
                max=i
        return max
sk=Solution()

print("max element:",sk.maxElement([1,2,20,3,4,30,87,99,5,100]))
