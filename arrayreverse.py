def reverse(arr,index,end):
    while index<end:
        
        arr[index],arr[end]=arr[end],arr[index]
        index+=1
        end+=-1
    return arr
arr=[1,2,3,4]
print("reverse array:",reverse(arr,0,len(arr)-1))