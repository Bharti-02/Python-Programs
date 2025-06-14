# Count the Occurance 
def Count(number,target):
    count=0
    for i in range(len(number)):
        if number[i]==target:
           count+=1
    return count
    
number=list(map(int,input("Enter no:").split()))
target=int(input("Enter no:"))

print(Count(number,target))