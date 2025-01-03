# Factorial

def Factorial(num):
    if num<0:
        return "Negative number not supported in factorial"
    elif  num==0:
        return "Factorial of 0 is 1"
    else:
        fact=1
        for i in range(1,num+1):
           fact=fact*i
        return f"Factorial is {fact}"
num=int(input("enter number"))
print(Factorial(num))
