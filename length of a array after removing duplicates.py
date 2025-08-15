class Solution:
    
    def removeduplicatlength(self, arr):
        i=0
        n=0
        for j in range(1,len(arr)):
            if arr[i]!=arr[j]:
               i+=1
            
            else:
               n+=1
               i+=1
                
        
        return n
sk=Solution()
arr=[1,2,2,3,4,5,5,6,7,7,8]

print("length of a array after removing duplicates:",sk.removeduplicatlength(arr))