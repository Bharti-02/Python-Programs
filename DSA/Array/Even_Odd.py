#Count Even and Odd in  a array 

arr=list(map(int,input("Enter numbers:").split()))
Even=0
Odd=0
print(arr)
for i in arr:
	if i%2==0:
    		Even+=1
	else:
		Odd+=1
print("Even_numbers:",Even)
print("Odd_numbers:",Odd)
