def binary_search(arr,target):
    left,right=0,len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
           left=mid+1
           
        else:
            right=mid-1
    return -1

arr=[1,4,5,7,8,9,10]     
target=5
print("Index:",binary_search(arr,target))  
