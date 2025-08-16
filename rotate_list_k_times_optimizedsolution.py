def reverse(arr,index,end):
    while index<end:
        
        arr[index],arr[end]=arr[end],arr[index]
        index+=1
        end+=-1
    return arr
arr=[1,2,3,4]
k=1
k=k%len(arr)
reverse(arr,0,len(arr)-1)
reverse(arr,0,len(arr)-k-1)
print("rotate a array",k,"times:",reverse(arr,len(arr)-k,len(arr)-1))