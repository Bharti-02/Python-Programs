# Even Odd

def Even(a):
    if (a%2==0):
       return "Even "
    else:
        return "Odd"

a=int(input("enter number"))
result=Even(a)
print(result)
