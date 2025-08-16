class Solution:
    def rotate(self,arr):
        temp=arr[0]
        for i in range(0,len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp
        return arr
sk=Solution()
print("rotating array:",sk.rotate([1,2,3,4,5,6,7,8]))
