class Solution:
    
    def rotateArr(self, arr, d):
       
        k=[]
        j=[]
        for i in range(0,len(arr)):
            d=d%len(arr)
            if i<d:
                k.append(arr[i])
            else:
                j.append(arr[i])
        arr[:]=j+k
        return arr
sk=Solution()
print("rotating array:",sk.rotateArr(([1,2,3,4,5,6,7,8]),3))