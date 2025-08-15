class Solution:
    def reverseArray(self, arr):
        
        k=[]
        for i in range(len(arr)-1,-1,-1):
            k.append(arr[i])
        arr[:]=k
        return k
sk=Solution()
print(sk.reverseArray([1,2,3,4,5,5,6,7,8,9,10]))
