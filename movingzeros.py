class Solution:
	def pushZerosToEnd(self, arr):
         k=[]
         j=[]
         for i in arr:
              if i!=0:
                   k.append(i)
              elif i==0:
                   j.append(i)
         arr[:]=k+j
         return arr
sk=Solution()
print(sk.pushZerosToEnd([1,0,2,3,4,5,0,6,0,0,9]))
              
        