# find the frequency 

arr=[1,22,33,4,4,5,5,1,2,33,44]
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)