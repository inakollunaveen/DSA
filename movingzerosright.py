def movingzeros(arr):
    pos=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[pos]=arr[pos],arr[i]
            pos+=1
    return arr
arr=[1,0,3,0,5,0,0,6,7,8,0,0,0]
print("moving zeros to right:",movingzeros(arr))