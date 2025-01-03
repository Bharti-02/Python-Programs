# Largest

def Largest(a,b,c):
    if (a>b and a>c):
        return f"{a} is largest"
    elif(b>a and b>c):
        return f"{b} is largest"
    else:
        return f"{c} is largest"

a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))

print(Largest(a,b,c))
