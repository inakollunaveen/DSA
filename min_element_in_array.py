

class Solution:
    def minElement(self,nums):
        min=nums[0]
        for i in nums:
            if i<min:
                min=i
        return min
sk=Solution()

print("min element:",sk.minElement([1000,23,20,3,4,30,87,99,5,100]))
