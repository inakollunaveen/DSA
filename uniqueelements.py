class Solution:
    def Unique(self,arr):
        k=set()
        for i in arr:
            if i not in k:
                k.add(i)
        return list(k)
sk=Solution()
arr=[1,1,2,3,4,5,5,6,6,7,8,9]
print(f"Unique Elements:",sk.Unique(arr))