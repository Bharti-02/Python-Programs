# Linear Search
def Linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1
                
arr=list(map(int,input("Enter arr :").split()))
target=int(input("Enter target no :"))

print(Linear(arr,target))



   