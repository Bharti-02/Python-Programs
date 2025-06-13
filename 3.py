# Count even numbers in a list

nums = [1, 4, 6, 9, 10, 13]
count=0
for i in nums:
    if i %2==0:
        count+=1
print(count)