# remove duplicates from array

arr=[1,4,4,5,6,7,8,88,9]

unique=[]
for i in arr:
	if i not in unique:
		unique.append(i)

print(unique)