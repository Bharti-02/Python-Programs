# find Maximum and Minimum in an array

arr=[3,4,9,1,7]

largest=arr[0]
smallest=arr[1]

for i in arr:
	if i >largest:
		largest=i
	elif i<smallest:
    		smallest=i
print("Maximum number:",largest)
print("Minimum number:",smallest)


	

