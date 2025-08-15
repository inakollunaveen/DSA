class Solution:
    def sorted_are_not(self,nums):
        k=0
        for i in range(0,len(nums)-1):
            if nums[i]<=nums[i+1]:
                k+=1
            else:
                pass
        if k==len(nums)-1:
            return "SORTED ARRAY"
        else:
            return "unsorted array"
sk=Solution()
print(sk.sorted_are_not([1,2,3,3,4,4,5,5,99,10]))
